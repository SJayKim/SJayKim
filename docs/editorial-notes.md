# 작성 기준과 근거

2026-11-22에 국문 경력기술서와 1쪽 이력서를 다시 작성함. 경력기술서는 대표 프로젝트 4개와 추가 프로젝트 5개를 담아 현재 프로젝트에 치우쳤던 분량을 조정함. 이력서는 회사별 주요 기여와 확인된 성과를 한 쪽에 요약함. 비개발자도 이해할 수 있도록 해결하려던 문제와 맡은 일을 먼저 설명하고, 문장 어투는 음슴체로 통일함. README와 영문 이력서는 이번 변경에 포함하지 않음.

## 선택한 작성 방식

- 경력기술서: 비교안 ④를 선택함. Anthropic의 [doc-coauthoring](https://github.com/anthropics/skills/blob/main/skills/doc-coauthoring/SKILL.md)에서 독자·목적·구성을 정하고 독자 관점으로 다시 읽는 방식을 적용함. 회사별 전용 이력서 양식으로 소개하지 않음.
- 1쪽 이력서: 비교안 ②를 선택함. 커뮤니티 [cv-builder](https://github.com/claude-office-skills/skills/blob/main/cv-builder/SKILL.md)의 YAML·RenderCV 방식을 사용함. RenderCV 2.8의 classic 형식으로 PDF를 생성함.
- 비교안 ①·③: 특정 지원 공고가 정해졌을 때 경험 선택과 문장 조정에 활용할 예정임. 이번 기본 문서에 임의의 공고 키워드나 적합도 점수를 넣지 않음.

문장 검토에는 humanize-korean을 사용함. 독립 검토자가 읽기 전용으로 이해도·역할·수치·문체를 점검했으며, F1 비교 모델의 누락을 고치고 연결어미 뒤 쉼표와 어색한 조사를 정리함. 기술명과 수치, 미완료 상태는 보존함. 이전 [리뷰 기록](review.md)은 2026-11-21 작업에 대한 기록임.

## 문서 생성

Edit `resume.ko.yaml` for the Korean resume and `career-history.ko.md` for the career history. Run the following command from the repository root to generate both PDFs and `resume.ko.md`:

```sh
uv run docs/render_korean.py
```

The script pins its Python dependencies, including RenderCV 2.8. Install the Noto Sans CJK KR regular and bold fonts before rendering. Career PDF generation uses Google Chrome on macOS, or an installed Playwright Chromium browser on other systems. Inspect the generated PDFs after edits. The script checks page counts, key text extraction, and career-page overflow.

PDF links point to `main` by default. For a published branch preview, add `--link-ref <branch>`; this revision uses `--link-ref docs/career-resume-20261122`. Regenerate with the default after merging to keep links independent of the preview branch.

## 기존 정리 기준 (2026-11-21)

이전 정리는 Claude에서 작성한 [「미국 테크 이력서 작성 가이드와 자료 모음」](https://claude.ai/artifact/US2YiKg6LcuzFmoaxK1oBc)을 기준으로 함. 2026-11-21 작성 기록의 본문을 확인했으며 한 단 구성, 최근 경험 우선, 행동·결과 중심 문장, 수치의 사실 보존 원칙을 적용함. 개인 연락처는 기존에 공개된 이메일만 사용함.

## 문서별 적용

영문 이력서는 Experience·Projects·Skills·Education의 표준 제목과 텍스트 중심 형식으로 구성함. 핵심 성과만 남기고 기술 상세와 현재 프로젝트의 전체 구성은 경력기술서와 프로젝트 문서에 배치함. 특정 채용공고가 지정되지 않아 AI/ML·AI Agent 엔지니어의 기본 이력서로 작성함.

성과는 행동·관측한 결과·방법이 연결되도록 씀. 정량 성과가 확인되지 않은 현재 프로젝트에는 구현 범위와 검증 단계를 적었으며 생산성 개선율·매출·사용자 수를 만들지 않음. Company Brain과 DCA의 합성 시험은 실제 고객 업무 성과와 구분함.

프로젝트 이름은 대상과 기능을 먼저 드러내도록 정리함. 현재 작업의 대표 이름은 ‘AI 소프트웨어 유지보수 플랫폼’이며 내부 이름은 상세 문서의 대응표에 보존함. 기존 프로젝트도 ‘매거진 검색·추천 AI 챗봇’, ‘뉴스 요약·분류·태깅 API’처럼 사용자가 하는 일을 제목에 씀. ReAct·Reflexion, Milvus, vLLM 등 구현 기술은 본문에 남기고 Visit Busan·Skylife·MarketScope AI는 서비스·고객 맥락에서 표기함.

원칙의 공개 출처는 [Tech Interview Handbook](https://www.techinterviewhandbook.org/resume/), [Tech Resume Checklist](https://github.com/n2cholas/resume-checklist), [EngineeringResumes 작성 가이드](https://github.com/r-engineeringresumes/subreddit-wiki/blob/main/wiki/index.md)임. 2026-11-21 작업에서는 가이드에 소개된 외부 skill이나 이력서 업로드 서비스를 설치·실행하지 않음. 2026-11-22의 작성 방식과 PDF 생성 도구는 위에 별도로 기록함.

## 사용한 사실 자료

| 자료 | 사용 범위 |
| --- | --- |
| [기존 공개 README](https://github.com/SJayKim/SJayKim/blob/0edb6b69a507b3a8d819064b8483ba2b847261a9/README.md) | 이름·이메일·학력·기존 8개 프로젝트·공개 성과 수치 |
| Project Reliability 최신 구현 대응표·현재 인계, 통합 작업트리의 manifest·코드 구조 | Rust 제어부·Runner·CLI, 검증 및 배포 경계 |
| 고객 패널·운영 관제판 인계 | 단계 A 검증, P3·B/C 소스 작성과 검증 유예 |
| Relay·Context 최신 인계와 공통 모델 정의 | 인수·근거 조회·재확인·온톨로지 구현과 제한 |
| DCA 통합 시제품 인계 | 오프라인 분석·사람 검토·플랫폼별 합성 시험 결과 |
| Company Brain 최신 구현·검수 기록 | PostgreSQL 영속 저장·권한·복구, 원문 검색·검토, 로컬 Ollama 호출의 합성 검증과 미연결 범위 |
| 통합 설계·연결부 명세 | 전체 연결 목표와 7개 연결부의 책임 |

내부 자료에서는 공개 설명에 필요한 역할·기술·구현 상태만 추림. 고객 원문, 계약·금액, 내부 저장소 주소, 실행 식별자와 자격 정보는 포함하지 않음. 이 문서 작업을 위해 원 프로젝트의 실행·시험·배포를 재시작하지 않음.

프로젝트 이름을 재정리하면서 2026-11-21의 최신 구현 기록을 확인함. 업무 근거 검색·의사결정 지원 시스템은 최초 메모리 시제품 이후 PostgreSQL과 로컬 모델 연동을 구현함. 이전의 ‘영속 저장·모델 연결 전’ 설명을 갱신했으며 실제 회사 원천·인증·운영 연동과 업무 효용 검증은 계속 미완료로 표기함. 해당 구현·검수 문서에 기록된 결과를 인용했으며 이번 포트폴리오 작업에서 제품 검사를 재실행하지 않음.

## 정정한 표현

| 기존 표현 | 이번 처리 |
| --- | --- |
| 스미싱 F1 28.79%→96.10% | 28.79%는 9:1, 96.10%는 1:1 평가임. 같은 1:1 조건에서 기존 Random Forest의 58.02%와 추가 학습한 URLBert의 96.10%를 비교함. 같은 모델의 학습 전후 비교로 표현하지 않음 |
| GEval 호출 수와 토큰 비용을 함께 1/5로 축소, 품질 유지 | 5개 기준의 평가 요청을 1회로 통합한 구조만 사용. 비용·품질 동등성은 별도 측정 필요 |
| vLLM 도입으로 외부 API 비용 100% 제거 | 해당 작업의 자체 서빙 전환으로 기술. 총 인프라 비용 절감으로 확대하지 않음 |
| 응답 시간 약 65%, Recall 약 35%, 재시도 약 55% 개선 | 비교 환경·평가 집합·측정 기간의 원자료가 없어 제출용 요약에서 제외 |
| Visit Busan·MarketScope가 현재 운영 중 | 공개 기록 시점의 서비스 적용·공개 이력으로 기술. 현재 상태는 재확인하지 않음 |
| AWS/Kubernetes 학습·향후 배포 | 현재 운영 경험에 포함하지 않음 |
| Company Brain·Context·Reliability가 연결된 운영 시스템 | 개별 구현, 합성 검증, 연결 설계, 남은 운영 검증을 구분 |

## 제출 전에 확인할 사실

- 회사별 공식 입·퇴사 연월과 직함. 프로젝트 기간을 재직기간으로 대신하지 않음.
- 대상 공고, 근무 희망 지역, LinkedIn 등 추가 연락처. 확인되지 않은 개인정보·취업 자격은 기재하지 않음.
- 과거 수치의 평가 집합·측정 환경·기간. 현재 문서에는 기존 공개 수치를 인용했으며 재평가는 수행하지 않음.
- 현재 프로젝트의 팀 규모와 개인별 세부 기여율. 전체 작업을 단독 수행했다고 표현하지 않음.

2026-11-21 작업에서 README의 기존 기술 상세를 [기존 프로젝트 문서](projects/prior-projects.md)로 재구성함. 이전 원문과 도표는 Git 이력에서 확인할 수 있으며 기존 이미지 파일은 보존함. 2026-11-22 작업에서는 README를 수정하지 않음.
