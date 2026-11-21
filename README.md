# 김선준 | Sunjun Kim

AI/ML 엔지니어. 검색·추천, LLM 서빙·평가, 업무 에이전트를 개발합니다. 현재는 **Project Reliability와 연계 시스템**에서 AI가 유지보수 작업을 수행할 때 필요한 맥락, 검증, 승인 흐름을 설계·개발하고 있습니다.

[영문 이력서](docs/resume.en.md) · [PDF](docs/resume.en.pdf) · [국문 이력서](docs/resume.ko.md) · [경력기술서](docs/career-history.ko.md) · [전체 문서](docs/README.md)

연락처: [cyon13022@gmail.com](mailto:cyon13022@gmail.com) · [GitHub](https://github.com/SJayKim)

## 주요 성과

- URLBert 파인튜닝으로 스미싱 탐지 F1을 **58.02% → 96.10%**로 개선했습니다. 같은 1:1 균형 평가 조건의 비교입니다.
- 약 **60만 건** 규모의 뉴스 요약을 평가·적재·보고하는 파이프라인을 구축했습니다. 5개 품질 기준을 단일 GEval 요청에 묶고 증분 처리와 정기 실행을 자동화했습니다.
- 5명 팀에서 AI 파트를 맡아 자연어 여행 의도와 벡터 검색을 결합한 Visit Busan 여행 챗봇을 개발했습니다.
- 개인 프로젝트 MarketScope AI에서 **서울시 1,650개 상권** 데이터와 11종 도구를 지도·AI 에이전트에 연결했습니다.

위 성과는 기존 공개 프로젝트 기록 기준입니다. 평가 조건과 프로젝트별 상태는 [상세 문서](docs/projects/prior-projects.md)에 정리했습니다.

## 현재 프로젝트: Project Reliability

고객 프로젝트의 인수 자료를 구조화하고, 유지보수 요청의 근거를 확인한 뒤 AI 에이전트가 격리된 환경에서 수정·시험하도록 제어하는 시스템입니다. Rust 제어부·Runner·CLI, PostgreSQL 작업 큐, 모델 호출 예산, 외부 변경 기록을 개발하고 있습니다.

| 구성 | 역할 | 현재 상태 |
| --- | --- | --- |
| Reliability 핵심 | 요청·상태·정책, 격리 실행, 검증, 게시·감사, 모델 예산 | Rust 구현 대체 및 일부 실제 연동 검증. 후속 품질 검증 진행 |
| 고객 패널 | 업무 흐름·고객 상태 조회, 후속 요청·응답·승인 설계 | P2 게이트웨이 로컬 구현, P3 조회 소스 작성·검증 유예. P4~P7 미구현 |
| 운영 관제판 | 작업 상태·비용·주의 항목 관측 | 단계 A 합성 검증 완료. B/C 검증·통합 전 |
| AIDP Relay | 기능·코드·환경·검증 근거를 연결한 인수·인계 | 로컬 구현. 실제 인수는 조건부 상태 |
| Context App·FDE Ontology | 근거 조회·판·권한 재확인, 공통 업무 모델 | 로컬 구현 및 한정된 기술 수락. 전체 운영 검증 전 |
| Data Connection Analysis | 데이터 사전, 키·관계 후보, 사람 검토 목록 | 오프라인 로컬 시제품·합성 시험 |
| Company Brain | 근거 브리핑, 상충·정정 표시, 원문 대조 | 합성 자료 기반 로컬 시제품 |
| Reliability Demo | 요청·계획·검토·승인 흐름의 HTML 시연 | 가상 처리 소스 구현. 브라우저·시나리오 검증 전 |
| 통합 계약 | 식별 매핑부터 실행 전 확인·결과 환류까지 7개 연결부 | 설계와 일부 합성 검증. 전체 운영 연동 전 |

기준일: 2026-11-21. 구성요소별 구현·검증을 진행하고 있으며 자동 merge·배포, AWS 운영, 실제 고객 업무 효과는 완료 실적에 포함하지 않았습니다.

[전체 시스템·아키텍처·기여·검증 상태](docs/projects/project-reliability.md)

## 기존 프로젝트

| 프로젝트 | 담당·핵심 내용 | 상세 |
| --- | --- | --- |
| 뉴스 요약 LLM 평가 · Plantynet | 약 60만 건 규모, GEval·증분 처리·PostgreSQL·정기 보고 | [평가 파이프라인](docs/projects/prior-projects.md#한국어-뉴스-요약-llm-평가-파이프라인) |
| URL 스미싱 탐지 · Plantynet | URLBert 파인튜닝, 동적 URL·HTML 분석, 성능 모니터링 | [모델·평가 조건](docs/projects/prior-projects.md#url-기반-스미싱-탐지) |
| ReAct·Reflexion Agent · Plantynet | 17개 업무 도구, 실패 교훈 재사용, LightRAG 근거 검색 | [업무 에이전트](docs/projects/prior-projects.md#reactreflexion-업무-에이전트) |
| Agentic RAG · Plantynet | Milvus Dense·Sparse 검색, reranker, LlamaGuard | [검색·전처리](docs/projects/prior-projects.md#milvus-기반-agentic-rag) |
| vLLM API · Plantynet | 요약·분류·태깅 자체 서빙, LangGraph 처리 흐름 | [LLM 서빙](docs/projects/prior-projects.md#vllm-텍스트-처리-api) |
| Visit Busan 여행 챗봇 · AIO2O | AI 파트 리드, 관광지·리뷰 임베딩, 추천·일정 구성 | [여행 챗봇](docs/projects/prior-projects.md#부산관광공사-여행-스케줄링-챗봇) |
| Skylife 영화 추천 · AIO2O | pgvector, 메타데이터 필터·의미 유사도 추천 | [추천 시스템](docs/projects/prior-projects.md#skylife-영화-추천) |
| MarketScope AI · 개인 | 1인 개발, 상권 분석 Agent, 지도·대화 동기화 | [전체 개발 범위](docs/projects/prior-projects.md#marketscope-ai) |

## 기술

| 분야 | 사용 기술 |
| --- | --- |
| AI Agent·평가 | LangGraph, ReAct/Reflexion, LightRAG, deepeval/GEval, Langfuse, MCP |
| 모델·검색 | vLLM, Hugging Face Transformers, BERT, BGE-M3, BM25, reranker, Milvus, pgvector |
| 서비스·데이터 | Python, Rust, TypeScript, FastAPI, axum, SQLx, PostgreSQL/PostGIS, SQLite, React |
| 실행·검증 | Docker, Docker Compose, Playwright, GitLab, cron/flock |

## 학력·집필

UNIST 산업공학과 석사, 2023. 추천 시스템의 잠재 표현과 조건부 증강을 연구했습니다. 학위 논문: [Personal recommender system via convolutional autoencoder with conditioning augmentation](https://apac-tc.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=82UNIST_INST21228494070002596&vid=82UNIST&search_scope=everything&tab=everything&lang=ko_KR&context=L).

Wikidocs [『Agentic AI: 스스로 진화하는 인공지능 에이전트 만들기』](https://wikidocs.net/book/19070)에 에이전트 연구와 구현 자료를 정리합니다.

[작성 기준·출처·확인 범위](docs/editorial-notes.md) · [1회 재검토 기록](docs/review.md)
