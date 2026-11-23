# 포트폴리오 도식

README의 프로젝트 9개와 유지보수 플랫폼 상세 문서의 전체 연결 목표를 Archify로 통일했다. [도식 모음](https://sjaykim.github.io/SJayKim/docs/diagrams/)에서 탐색할 수 있다. 실제 서비스 화면 캡처와 과거 자료는 보존했다.

## 근거와 수정 기록

확인일은 2026-11-23이다. 회사 프로젝트 8개는 공개된 경력 문서와 기존 구성도를 근거로 작성한 개념도다. 회사 원본 코드나 현재 운영 상태를 재검증한 결과가 아니다. 각 JSON은 근거 저장소의 커밋과 문서 줄 번호를 고정한다. 구성요소의 상세 역할과 상태 설명은 HTML의 설명 카드에 남겼다.

MarketScope는 공개 코드 `78aeb1b759e599ce6cc70f9b6697bb1cb1b9939c`의 실행 분기, 도구 호출, 캐시 접근과 최종 본문 검증 경로를 확인했다. 기존 상세 문서의 PAE 구조·11종 도구·시험 수치는 과거 기록으로 보존하고 현재 코드와 구분했다.

| 확인한 부분 | 반영 |
| --- | --- |
| MarketScope의 과거 PAE 설명과 최근 v2 도식의 기준 시점 차이 | 상세 문서에 현재 코드 판과 v2·Mock/PAE 실행 조건을 추가 |
| MarketScope 도식이 Redis 접근을 Repository 한 곳으로 표현 | 도구와 지도 API의 직접 캐시 조회·저장을 표시. 벤치마크 Repository의 캐시 접근도 설명에 명시 |
| MarketScope의 “검증 후 전송” 범위 | 최종 답변 본문과 먼저 전송될 수 있는 진행 이벤트·결과 카드를 구분 |
| 유지보수 도식의 작업 저장소→대시보드 “조회” 방향 | 읽기 주체가 드러나도록 대시보드→저장소의 “읽기 조회”로 변경 |
| 고객 접점의 조회 구현·검증 상태 | P2 로컬 구현, P3 실행 검증 전, 요청·승인 미구현을 도식에 명시 |

회사 프로젝트의 개인 기여 범위, 개발 중인 상태와 평가 조건은 보존했다. 요약 평가의 5회→1회 호출 통합을 비용 1/5 절감으로 표현하지 않았고, 스미싱 F1은 같은 1:1 평가 조건의 58.02%→96.10% 비교를 유지했다. 운영 시험과 모델 평가를 새로 실행하지 않았다.

## Editing and verification

Each `<slug>.json` is the editable Archify source. The matching HTML is the standalone viewer, and `../../images/architecture/<slug>.png` and `.svg` are canonical viewer exports. Edit JSON, then regenerate HTML and both previews together. Do not patch generated HTML.

Use Archify 3.2.0 from its installed skill directory. Run from the portfolio repository root:

```sh
node "$ARCHIFY_ROOT/bin/archify.mjs" finalize architecture \
  "docs/diagrams/$slug.json" "docs/diagrams/$slug.html" \
  --repo-root "$SOURCE_REPO" --quality showcase \
  --out-dir "$REVIEW_DIR" --json
```

`SOURCE_REPO` is a checkout of the repository and revision pinned in the candidate: this portfolio for company diagrams, Catchment-Area-Analysis for MarketScope. Give each subsequent review a fresh directory. Keep local receipts outside the public repository because they contain host paths. Export PNG and dual-theme SVG through the checked viewer, inspect both themes and the resulting preview, and verify README links. Do not infer product validation from diagram checks.

The Pages workflow publishes only HTML viewers and diagram images. JSON sources remain available through GitHub. The gallery and README link to the deployed viewers; GitHub renders the PNG previews directly. Before publishing, verify the gallery at desktop and mobile widths, source links, viewer interaction, and all ten outputs.
