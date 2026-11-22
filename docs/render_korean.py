# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "rendercv[full]==2.8",
#   "playwright==1.65.2",
#   "markdown-it-py==4.0.0",
#   "PyYAML==6.0.4",
#   "pypdf==6.1.3",
# ]
# ///
"""Build the Korean resume and career PDFs: uv run docs/render_korean.py.

Edit resume.ko.yaml and career-history.ko.md, then run this script.
The resume Markdown and PDF are generated from the same YAML source.
Requires a Korean font configured in the YAML, plus Google Chrome on macOS
or a Playwright Chromium installation on other systems.
"""

from html import escape
from pathlib import Path
import argparse
import json
import re
import shutil
import subprocess
import tempfile
from urllib.parse import urljoin

from markdown_it import MarkdownIt
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
import yaml


ROOT = Path(__file__).resolve().parent
PAGE_BREAK = "<!-- pagebreak -->"
STYLE = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; color: #202a33; font-family: var(--font), sans-serif; }
.page { width: 210mm; height: 297mm; padding: 14mm 16mm 18mm; position: relative; break-after: page; }
.page:last-child { break-after: auto; }
.content { font-size: 10.5pt; line-height: 1.5; }
h1 { color: #004f90; font-size: 23pt; line-height: 1.2; margin: 0 0 3mm; }
h2 { color: #004f90; font-size: 13pt; line-height: 1.3; border-bottom: .3mm solid #8baaca; padding-bottom: 1.4mm; margin: 5mm 0 3mm; }
.content > h2:first-child { margin-top: 0; }
p { margin: 1.8mm 0; }
p:has(> strong:only-child) { font-size: 11.5pt; margin: 4.5mm 0 1.2mm; }
ul { padding-left: 5mm; margin: 2mm 0; }
li { padding-left: .3mm; margin: 1.7mm 0; }
li p { margin: 0; }
a { color: #004f90; text-decoration: none; }
em { font-style: italic; }
.footer { position: absolute; bottom: 8mm; left: 16mm; right: 16mm; display: flex; justify-content: space-between; border-top: .2mm solid #ccd6e0; padding-top: 2mm; color: #607080; font-size: 8pt; }
"""


def resume_markdown(cv):
    lines = [
        "<!-- Generated from resume.ko.yaml by render_korean.py; edit the YAML source. -->",
        f"# {cv['name']} (Sunjun Kim)",
        cv["headline"],
        f"[{cv['email']}](mailto:{cv['email']}) · "
        "[GitHub](https://github.com/SJayKim) · [1쪽 PDF](resume.ko.pdf) · "
        "[경력기술서](career-history.ko.md)",
    ]
    for title, entries in cv["sections"].items():
        lines.append("## " + title)
        for entry in entries:
            if isinstance(entry, str):
                lines.append(entry)
            elif "name" in entry:
                lines.extend([
                    "**" + entry["name"] + "**", entry["date"],
                    "\n".join("- " + item for item in entry["highlights"]),
                ])
            elif "label" in entry:
                lines.append("- " + entry["label"] + ": " + entry["details"])
            else:
                raise ValueError(f"Unsupported resume entry in {title}")
    return "\n\n".join(lines) + "\n"


def career_html(source, font, public_docs):
    renderer = MarkdownIt("commonmark", {"html": False})
    sections = source.split(PAGE_BREAK)
    pages = []
    for number, section in enumerate(sections, 1):
        body = renderer.render(section.strip())
        body = re.sub(
            r'href="([^\"]+)"',
            lambda match: 'href="' + escape(urljoin(public_docs, match[1]), quote=True) + '"',
            body,
        )
        pages.append(
            '<section class="page"><main class="content">' + body + '</main>'
            '<footer class="footer"><span>김선준 · 경력기술서</span>'
            f'<span>{number} / {len(sections)}</span></footer></section>'
        )
    return (
        '<!doctype html><html lang="ko"><head><meta charset="utf-8">'
        '<title>김선준 경력기술서</title><style>' + STYLE + '</style></head>'
        '<body style="--font:' + escape(json.dumps(font, ensure_ascii=False), quote=True) + '">'
        + ''.join(pages) + '</body></html>'
    )


def verify_pdf(path, expected_pages):
    reader = PdfReader(path)
    if len(reader.pages) != expected_pages:
        raise ValueError(f"{path.name}: expected {expected_pages} pages, got {len(reader.pages)}")
    text = "\n".join(page.extract_text() for page in reader.pages)
    compact = re.sub(r"\s+", "", text)
    for anchor in ["김선준", "58.02%", "96.10%", "Random Forest", "60만", "1,650"]:
        if re.sub(r"\s+", "", anchor) not in compact:
            raise ValueError(f"{path.name}: missing text anchor {anchor}")
    return len(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--link-ref", default="main", help="Published Git ref for links embedded in the PDFs")
    args = parser.parse_args()
    public_docs = f"https://github.com/SJayKim/SJayKim/blob/{args.link_ref}/docs/"
    yaml_source = (ROOT / "resume.ko.yaml").read_text()
    data = yaml.safe_load(yaml_source)
    markdown = resume_markdown(data["cv"])
    career = (ROOT / "career-history.ko.md").read_text()
    with tempfile.TemporaryDirectory(prefix="sunjun-profile-") as folder:
        temp = Path(folder)
        render_yaml = temp / "resume.yaml"
        render_yaml.write_text(yaml_source.replace("(career-history.ko.md)", f"({public_docs}career-history.ko.md)"))
        resume_pdf = temp / "resume.ko.pdf"
        subprocess.run([
            "rendercv", "render", str(render_yaml),
            "--output-folder", str(temp / "rendercv"),
            "--pdf-path", str(resume_pdf),
        ], check=True)
        resume_chars = verify_pdf(resume_pdf, 1)
        html_path = temp / "career-history.ko.html"
        html_path.write_text(career_html(career, data["design"]["typography"]["font_family"], public_docs))
        career_pdf = temp / "career-history.ko.pdf"
        with sync_playwright() as pw:
            chrome = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
            options = {"executable_path": str(chrome)} if chrome.is_file() else {}
            browser = pw.chromium.launch(headless=True, **options)
            try:
                page = browser.new_page()
                page.goto(html_path.as_uri(), wait_until="load")
                page.evaluate("document.fonts.ready")
                boxes = page.evaluate("""() => [...document.querySelectorAll('.page')].map(p => ({
                    content: p.querySelector('.content').getBoundingClientRect().bottom,
                    footer: p.querySelector('.footer').getBoundingClientRect().top
                }))""")
                for index, box in enumerate(boxes, 1):
                    if box["content"] > box["footer"] - 8:
                        raise ValueError(f"Career page {index} overlaps its footer; shorten the source or adjust spacing")
                page.pdf(path=str(career_pdf), format="A4", print_background=True, prefer_css_page_size=True)
            finally:
                browser.close()
        career_chars = verify_pdf(career_pdf, len(career.split(PAGE_BREAK)))
        (ROOT / "resume.ko.md").write_text(markdown)
        shutil.copyfile(resume_pdf, ROOT / "resume.ko.pdf")
        shutil.copyfile(career_pdf, ROOT / "career-history.ko.pdf")
    print(json.dumps({
        "resume_pages": 1, "career_pages": len(boxes),
        "resume_text_characters": resume_chars, "career_text_characters": career_chars,
        "layout_overflow": False,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
