# 김선준 (Sunjun Kim)

AI/ML 엔지니어 | AI Agent · 검색 · 평가 · 모델 서빙

[cyon13022@gmail.com](mailto:cyon13022@gmail.com) · [GitHub](https://github.com/SJayKim) · [상세 경력기술서](career-history.ko.md)

추천 시스템 연구를 바탕으로 벡터 검색, LLM 서빙, 평가 자동화와 업무 에이전트를 개발했다. 현재는 AI 소프트웨어 유지보수 플랫폼에서 AI 유지보수의 근거·검증·승인 흐름을 설계·개발하고 있다. UNIST 산업공학과 석사.

## 경력 및 주요 프로젝트

**위시켓 | AI 소프트웨어 유지보수 플랫폼**

2026.11 기준 진행 중인 개발 프로젝트

- Rust 제어부·격리 Runner·운영자 CLI, PostgreSQL 작업 큐, 모델 호출 예산과 외부 변경 기록을 구현하며 AI 유지보수 실행 흐름을 구성했다.
- 소프트웨어 인수인계 검증, 코드·문서 검색, 업무·데이터 관계 모델, DB 분석, 고객 포털·대시보드를 포함한 전체 흐름과 7개 연결부를 설계했다.
- 업무 근거 검색·의사결정 지원 시스템에 PostgreSQL 권한 제어, 원문 대조·검토, 로컬 모델 연동을 구현했다. 합성 자료로 검증했으며 실제 회사 원천·운영 연동은 진행 전이다.

**Plantynet | AI 모델·검색·서빙·평가 프로젝트**

평가 파이프라인 수행 기간: 2026.01~2026.07

- 약 60만 건 규모의 뉴스 요약 평가 파이프라인을 구축했다. 품질 기준 5개를 단일 GEval 요청으로 묶고 증분 처리·PostgreSQL 적재·일일 보고를 자동화했다.
- URLBert 파인튜닝으로 1:1 균형 평가의 F1을 58.02%에서 96.10%로 개선하고, HTML 피처 17개를 쓰는 동적 URL 분석을 별도로 구현했다.
- Milvus 하이브리드 검색·reranker, vLLM 자체 서빙 API, 17개 업무 도구를 연결한 LangGraph ReAct·Reflexion 에이전트를 개발했다.

**AIO2O | 추천 시스템·여행 챗봇 프로젝트**

확인된 프로젝트 수행 기간: 2023.06~2024.10

- 부산관광공사 여행 챗봇의 5명 팀에서 AI 파트를 리드했다. 관광지·리뷰 임베딩과 메타 필터를 결합해 자연어 추천과 일정 구성을 구현했다.
- Skylife 영화 추천에서 PostgreSQL·pgvector를 이용해 장르·배우 조건과 영화 설명의 벡터 유사도를 결합한 추천 API를 개발했다.

## 개인 프로젝트

**지도 기반 상권 분석 AI 서비스 | 1인 Full-stack 개발 | 2026.01 시작**

MarketScope AI에 서울시 1,650개 상권 데이터를 적재하고 지도 기반 분석 서비스를 개발했다. LangGraph Planner·Actor·Evaluator와 11종 도구, 지도·챗봇 동기화, SSE 응답·리포트 카드를 구현했다. 상태와 수치는 2026-09 공개 기록 기준이다.

## 기술

Python, Rust, TypeScript · LangGraph, vLLM, Hugging Face Transformers, deepeval · FastAPI, React · PostgreSQL, SQLite, Milvus, pgvector · Docker, Playwright, MCP, GitLab.

## 학력·집필

UNIST 산업공학과 석사, 2023. 추천 시스템 학위 논문: *Personal recommender system via convolutional autoencoder with conditioning augmentation*.

Wikidocs [『Agentic AI: 스스로 진화하는 인공지능 에이전트 만들기』](https://wikidocs.net/book/19070) 집필.

표기한 기간은 프로젝트 기록 기준이다. 회사별 재직기간과 공식 직함은 별도 확인이 필요하다.
