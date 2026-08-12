# 김선준 | Sunjun Kim — AI Engineer

> Agentic AI와 RAG를 실제 백엔드 서비스와 운영 환경까지 연결해 온 4년차 AI Engineer

`Python` `LangGraph` `LLM` `RAG` `Tool Use` `FastAPI` `Milvus` `vLLM` `Docker` `Langfuse`

[MarketScope Live](https://marketscope.robitlabs.co.kr/) · [Lite 포트폴리오 핵심 요약](#selected-work) · [Agentic AI 연구 자료](https://wikidocs.net/book/19070)

## Selected Work

### 1. ReAct + Reflexion 자기 개선형 AI 에이전트

- LangGraph로 Actor → Evaluator → Reflection → 장기 기억 흐름을 설계하고 10여 종 업무 도구를 연결했습니다.
- Agent와 MCP Server를 분리 배포하고 trace·token·latency·error 관측 기준을 연결했습니다.
- 초기 운영 로그 기준 동일 유형 작업의 평균 재시도가 약 55% 감소했습니다. 표본 수와 절대값을 새로 추정하지 않은 관찰 결과입니다.

### 2. Milvus Agentic RAG

- 약 15만 건 전처리, Milvus Vector DB, Dense/BM25 하이브리드 검색, Reranker, Safety Layer를 구현했습니다.
- 동일 평가셋에서 기존 키워드 검색 대비 전체 검색 경로의 Top-5 Recall이 약 35% 향상됐습니다.
- 담당 범위는 전처리·Vector DB·검색 엔진이며, 에이전트 로직은 동료가 주도하고 로직 설계에 부분 참여했습니다.

### 3. MarketScope AI

- LangGraph Tool Calling과 지도 UI를 결합한 상권분석 서비스를 기획부터 백엔드·배포·회귀 테스트까지 1인 개발했습니다.
- 서울 1,650개 상권 데이터를 제공하며 Chromium E2E 66/66, 프로덕션 스모크 28/28을 통과했습니다.
- Live: [marketscope.robitlabs.co.kr](https://marketscope.robitlabs.co.kr/)

## Research

- [Wikidocs — Agentic AI](https://wikidocs.net/book/19070)
- [Inside the Scaffold: A Source Code Taxonomy of Coding Agent Architectures](https://www.notion.so/76-Inside-the-Scaffold-A-Source-Code-Taxonomy-of-Coding-Agent-Architectures-341736a271928198b64adeca0b3eec43)

## Contact

- Email: [cyon13022@gmail.com](mailto:cyon13022@gmail.com)
