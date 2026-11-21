# /// script
# requires-python = ">=3.9"
# dependencies = ["reportlab==4.4.5"]
# ///
"""Render the English Markdown resume: uv run docs/render_resume.py.

Uses a single US Letter column and standard Helvetica at 10.2 pt or larger.
The Markdown file is the content source; unsupported blocks fail explicitly.
"""

from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate


ROOT = Path(__file__).resolve().parent


def inline(text):
    text = escape(text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)",
                  r'<link href="\2" color="#172f48">\1</link>', text)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)


def render():
    base = ParagraphStyle(
        "body", fontName="Helvetica", fontSize=10.2, leading=12.4,
        textColor=colors.HexColor("#151515"), alignment=TA_LEFT,
        spaceAfter=4,
    )
    styles = {
        "body": base,
        "name": ParagraphStyle("name", parent=base, fontName="Helvetica-Bold",
                               fontSize=22, leading=26, spaceAfter=4),
        "section": ParagraphStyle("section", parent=base,
                                  fontName="Helvetica-Bold", fontSize=11.4,
                                  leading=14, spaceBefore=8, spaceAfter=4,
                                  keepWithNext=True),
        "role": ParagraphStyle("role", parent=base, spaceBefore=3,
                               spaceAfter=4, keepWithNext=True),
        "bullet": ParagraphStyle("bullet", parent=base, leftIndent=10,
                                 bulletIndent=0, bulletFontSize=10.2, spaceAfter=3),
    }
    story = []
    source = (ROOT / "resume.en.md").read_text()
    for block in re.split(r"\n\s*\n", source.strip()):
        if block.startswith("# "):
            story.append(Paragraph(inline(block[2:]), styles["name"]))
        elif block.startswith("## "):
            story.append(Paragraph(inline(block[3:]), styles["section"]))
        elif block.startswith("- "):
            for item in re.split(r"\n(?=- )", block):
                story.append(Paragraph(inline(item[2:]), styles["bullet"],
                                       bulletText="-"))
        else:
            if block.startswith(("|", "```", "###")):
                raise ValueError("Unsupported resume block")
            style = styles["role"] if block.startswith("**") else base
            html = "<br/>".join(inline(line.strip())
                              for line in block.splitlines())
            story.append(Paragraph(html, style))
    target = ROOT / "resume.en.pdf"
    document = SimpleDocTemplate(
        str(target), pagesize=letter,
        leftMargin=36, rightMargin=36, topMargin=30, bottomMargin=30,
        title="Sunjun Kim - AI / ML Engineer", author="Sunjun Kim",
        subject="AI agents, retrieval, evaluation and model serving",
    )
    document.build(story)
    print(target)


if __name__ == "__main__":
    render()
