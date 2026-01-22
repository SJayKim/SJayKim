# Portfolio

## 소개

UNIST(울산과학기술원) 산업공학과 석사 졸업 (2023)

LLM 기반 AI 서비스 개발 경험을 보유한 백엔드/AI 엔지니어입니다. vLLM, LangGraph, RAG 시스템 구축부터 데이터 파이프라인, API 서비스까지 End-to-End 개발 경험이 있습니다.

## 학위 논문

**Personal recommender system via convolutional autoencoder with conditioning augmentation**

Recommender system and representation learning with convolutional autoencoder

Kim, Sunjun (2023) | UNIST 산업공학과 석사

[논문 링크](https://apac-tc.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=82UNIST_INST21228494070002596&vid=82UNIST&search_scope=everything&tab=everything&lang=ko_KR&context=L)

---

## 프로젝트 목록

| 구분 | 프로젝트 | 설명 | 역할 |
|------|----------|------|------|
| AIO2O | [Skylife 영화 추천 시스템](#aio2o-1-skylife-영화-추천-시스템) | 임베딩 벡터 기반 영화 추천 | 벡터 DB 구축, 추천 알고리즘 |
| AIO2O | [부산관광공사 여행 챗봇](#aio2o-2-부산관광공사-여행-스케줄링-챗봇) | 여행지 추천 챗봇 (상용 서비스) | 벡터 DB 구축, 추천 알고리즘 |
| Plantynet | [AI_LLM_API](#plantynet-3-ai_llm_api) | vLLM 기반 텍스트 처리 API 서비스 | 전체 개발 |
| Plantynet | [RAG 시스템](#plantynet-4-rag-시스템-ai_prompt--rag-chatbot) | Milvus 기반 Agentic RAG 챗봇 | 데이터 전처리, 벡터 DB, 검색 |
| Plantynet | [Planner MCP Host](#plantynet-5-planner-mcp-host) | AI 기획 산출물 자동 생성 시스템 | 전체 개발 |
| Side Project | [서울 상권분석 시스템](#side-project-6-서울-상권분석-시스템-sbiz_db--sbiz_llm) | 상권 데이터 수집 및 LLM Agent 분석 | 전체 개발 |

---

## 기술 스택

| 분류 | 기술 |
|------|------|
| Language | Python |
| LLM/AI | vLLM, LangChain, LangGraph, LiteLLM, OpenAI API, HuggingFace |
| Vector DB | Milvus, Pgvector |
| Database | PostgreSQL, Oracle, Mysql |
| Backend | FastAPI, Uvicorn |
| Frontend | Streamlit, Gradio |
| Infra | Docker, Docker Compose |
| Embedding | BGE-M3, BGE-Reranker, Sentence-Transformers |
| Protocol | MCP (Model Context Protocol), SSE, JSON-RPC |

---

## 프로젝트

### [AIO2O] 1. Skylife 영화 추천 시스템

**역할**: 벡터 DB 구축, 추천 알고리즘 개발

임베딩 벡터 기반 영화 콘텐츠 추천 시스템. 영화 메타데이터를 벡터화하여 의미 기반 유사도 검색 구현.

**주요 기능**
- 영화 메타 정보 임베딩 (장르, 내용, 감독, 배우 등)
- PostgreSQL + pgvector 기반 벡터 DB 구축
- 메타 필터링 + 벡터 유사도 결합 추천 알고리즘

**추천 알고리즘**
- 1단계: 메타 필터링 (장르, 배우, 감독 조건 적용)
- 2단계: 벡터 유사도 검색 (영화 설명/내용 의미적 유사도)

**기술 스택**: Python, PostgreSQL, pgvector, Embedding Models

---

### [AIO2O] 2. 부산관광공사 여행 스케줄링 챗봇

**역할**: 벡터 DB 구축, 추천 알고리즘 개발

자연어 질의 기반 여행 관광지 추천 챗봇. 현재 부산관광공사에서 상용 서비스 중.

**주요 기능**
- 여행지 관련 메타 데이터 임베딩 및 벡터 DB 구축
- 메타 필터링 + 벡터 유사도 결합 추천 알고리즘
- 여행 스케줄링 기능

**추천 알고리즘**
- 1단계: 메타 필터링 (지역, 여행 기간 1박/2박, 카테고리 등 조건 적용)
- 2단계: 벡터 유사도 검색 (여행지 설명, 후기, 활용 정보 의미적 유사도)

**서비스 링크**: [Visit Busan](https://www.visitbusan.net/index.do?menuCd=DOM_000000203018000000)

**기술 스택**: Python, Embedding Models, Vector DB, NLP

---

### [Plantynet] 3. AI_LLM_API

**역할**: 전체 개발 담당

LLM 기반 텍스트 처리 API 서비스. vLLM 엔진을 FastAPI 프로세스 내에서 직접 구동하여 효율적인 추론 파이프라인 구축.

**주요 기능**
- 기사 요약 API (목표 길이 수렴 알고리즘 적용, 70~130% 범위 내 수렴)
- 긴 문서 축약 (Map-Refine 파이프라인: 불릿 추출 -> 평문 기사 변환)
- 주제 분류 및 분류체계(Taxonomy) 분석
- 키워드/태그 추출 (구조화된 출력 기반)
- Gradio UI 제공 (Chatbot, Summarization, Topic/Taxonomy Classification)

**기술적 특징**
- vLLM LLMEngine in-process 아키텍처
  - 토큰 레벨 연속 배칭으로 동시 요청 효율 향상
  - asyncio.Semaphore로 최대 동시 LLM 연산 슬롯 관리
- LangGraph 기반 에이전트 구현
  - SummarizationAgent: target_text_instructions와 적응형 재시도(+-10%)
  - ReduceAgent: MAP-REFINE 파이프라인
  - KeywordAgent: 구조화된 출력 기반 태깅
  - AbstractAgent: 다중 기사 요약 통합
- API 버전 관리 (v0: 기본, v1: LangGraph 기반)

**API Endpoints**
```
POST /summarize_article         - 기사 요약
POST /summarize_magazine        - 긴문서 축약 (Map-Refine)
POST /classify_topic_from_article    - 주제 분류
POST /classify_taxonomy_from_article - 분류체계 분석
POST /generate                  - 자유 대화
```

**기술 스택**: Python, FastAPI, vLLM, LangGraph, LangChain, PyTorch, Gradio

---

### [Plantynet] 4. RAG 시스템 (AI_PROMPT + RAG-Chatbot)

**역할**: 데이터 전처리, 벡터 DB 구현, 검색 기능 구현

Milvus 기반 Agentic RAG 시스템. 한국어 매거진/문서 검색과 생성형 AI를 결합한 질의응답 챗봇.

**시스템 아키텍처**

```mermaid
flowchart LR
    subgraph Frontend
        User["User"]
        UI["Streamlit UI"]
    end

    subgraph Backend["FastAPI Service"]
        API["FastAPI"]
        Agent["LangGraph Agent"]
    end

    subgraph Safety["Safety Layer"]
        Guard["guard_input<br/>(LlamaGuard)"]
        Recheck["acall_model<br/>(Safety Re-check)"]
    end

    subgraph Tools["Tool Layer"]
        ToolNode["ToolNode<br/>(milvus_search)"]
        Retriever["MilvusRetriever"]
    end

    subgraph Storage
        Milvus[("Milvus DB<br/>(article_vectors)")]
    end

    User --> UI --> API --> Agent
    Agent --> Guard
    Guard -->|Pass| Recheck
    Guard -->|Block| API
    Agent --> ToolNode --> Retriever --> Milvus
    Recheck --> API
```

**주요 기능**

[검색 시스템]
- 하이브리드 검색: Dense 벡터 검색 + BM25 Sparse 키워드 검색 결합
- Reranking: BGE-Reranker-v2-M3 모델로 검색 결과 재정렬
- 컨텍스트 윈도우: 검색된 청크 주변 문맥 자동 확장 (window_size 설정)
- 날짜/매거진 필터링 지원

[Agent 시스템]
- Agentic RAG Loop: Safety Guard -> Reasoning -> Tool Calling -> Response
- LlamaGuard 기반 입출력 안전성 검증 (입력/출력 이중 검증)
- SSE 스트리밍 (token, message, timing, error 이벤트)
- Thread 기반 대화 히스토리 관리 (Checkpoint Store)
- MongoDB/PostgreSQL/SQLite 체크포인터 지원

**기술적 특징**

[임베딩 & 검색]
- BGE-M3 임베딩 모델 (1024차원 Dense Vector)
- BGE-Reranker-v2-M3 재정렬 모델
- COSINE 유사도 메트릭, nprobe=64
- 파라미터화된 검색 설정 (settings.py 중앙 관리)

[데이터 전처리]
- 100자 이상 청크 필터링
- 특수문자 제거 및 토큰 기반 검증
- KoNLPy 기반 한국어 텍스트 처리 최적화

[Agent 구현]
- LangGraph StateGraph 기반 그래프 구성
- AgentState: messages, remaining_steps, retrievals 관리
- wrap_model: SystemMessage 주입 + Tool 바인딩
- ToolNode로 milvus_search 실행 후 model로 재라우팅

**코드 구조**
```
src/agents/
  rag_assistant.py    - RAG Agent 그래프 정의 (guard_input -> model -> tools)
  milvus_tool.py      - MilvusRetriever 래퍼
  tools.py            - milvus_search 도구 등록
  llama_guard.py      - 안전성 검증
  milvus_key_search/  - 검색 엔진 코어

app/
  rag_api.py          - FastAPI 검색 API
  rag_query.py        - 쿼리 처리
```

**기술 스택**: Python, LangGraph, LangChain, FastAPI, Milvus, Streamlit, BGE-M3, BGE-Reranker, MongoDB, PostgreSQL

---

### [Side Project] 6. 서울 상권분석 시스템 (sbiz_db + sbiz_llm)

**역할**: DB 스키마 구성/구축, LLM 구현, Prompt 구현, 백엔드/프론트엔드 구현

서울 열린데이터광장 상권 데이터를 수집하고, LLM Agent로 분석하는 End-to-End 시스템.

**시스템 아키텍처**

```mermaid
flowchart TB
    subgraph DataPipeline["Data Pipeline - sbiz_db"]
        API_SRC["Seoul Open API<br/>(8 Services)"]
        Parse["APISpec Parser"]
        CSV["CSV Download"]
        ZIP["ZIP Extract"]
        DF["pandas DataFrame"]
        DB[("PostgreSQL")]
        
        API_SRC --> Parse --> CSV --> ZIP --> DF --> DB
    end

    subgraph LLMAgent["LLM Agent - sbiz_llm"]
        Chat["/chat API"]
        Router["route_query"]
        RAG["rag_agent"]
        ChatResp["chat"]
        Reject["reject"]
        Search["postgres_search"]
        Response["generate_response"]
        
        Chat --> Router
        Router --> RAG
        Router --> ChatResp
        Router --> Reject
        RAG --> Search --> Response
    end

    DB -.-> Search
```

**주요 기능**

[데이터 수집 - sbiz_db]
- 서울 Open API 8개 상권 서비스 자동 동기화
- APISpec 클래스로 HTML 파싱 -> 메타데이터/스키마 추출
- download/export_csv 메서드 지원 (fallback 처리)
- pandas DataFrame 컬럼 매핑 (한글 -> 영문)
- UPSERT 방식 중복 없이 저장
- CLI 지원: --inf-id, --sync-all, --list, --validate

[LLM Agent - sbiz_llm]
- 쿼리 라우팅: rag (상권 질문) / chat (일반 대화) / reject (거부)
- Tool Calling 기반 PostgreSQL 동적 검색
- 9개 상권 테이블 지원
- 비동기 처리 (asyncpg)

**지원 데이터 (9개 테이블)**

| 테이블 | 설명 | 주요 컬럼 |
|--------|------|-----------|
| trdar_relm | 상권 영역 (마스터) | trdar_cd, trdar_cd_nm, signgu_cd |
| trdar_selng | 추정 매출 | thsmon_selng_amt, ml/fml_selng_amt, 요일별/연령별 |
| trdar_stor | 점포 수 | stor_co, opbiz_stor_co, clsbiz_stor_co |
| trdar_flpop | 유동 인구 | tot_flpop_co, 성별/연령별/요일별 |
| trdar_rspop | 상주 인구 | tot_rspop_co, apt_hshold_co |
| trdar_wrcpop | 직장 인구 | tot_wrc_popltn_co, 성별/연령별 |
| trdar_rent | 임대료 | rent_area_div_avg, rent_fee_div_avg |
| trdar_ix | 상권 변화 지표 | trdar_chnge_ix, opbiz_rt, clsbiz_rt |
| trdar_fclty | 집객 시설 | 병원/은행/학교/지하철역 등 시설 수 |

**기술적 특징**

[데이터 동기화]
- inf_id 기반 서비스 정의 (OA-15560, OA-15572 등)
- 스키마 검증 후 DB 저장
- Primary Key 기반 UPSERT
- 크론잡 자동 동기화 지원

[LLM Agent]
- LangGraph StateGraph 기반 그래프
- Pydantic BaseModel로 Tool Input 스키마 정의
- PostgresSearchInput: table_name, stdr_yyqu_cd, trdar_cd, limit 등
- 시스템 프롬프트 중앙 관리 (src/core/prompts.py)

**코드 구조**
```
sbiz_db/
  data_sync.py        - 메인 동기화 서비스
  api_spec.py         - 서울 API 스펙 파서
  init_db/01_schema.sql - DB 스키마

sbiz_llm/src/
  agents/
    sbiz_agent.py     - LangGraph Agent
    tools/postgres_search.py - PostgreSQL 검색 도구
    subagents/query_router.py - 쿼리 라우팅
  core/
    settings.py       - Pydantic Settings
    prompts.py        - 시스템 프롬프트
  service/
    service.py        - FastAPI 서비스
```

**기술 스택**: Python, LangGraph, FastAPI, PostgreSQL, asyncpg, pandas, BeautifulSoup4, psycopg2, Docker

---

### [Plantynet] 5. Planner MCP Host

**역할**: 전체 개발 담당

LLM 기반 기획 산출물 자동 생성 시스템. MCP(Model Context Protocol) Host로서 다양한 LLM 프로바이더와 외부 도구를 통합하여 스토리 티켓, UX 플로우차트, IA(정보 아키텍처), 디자인 명세 등을 자동 생성.

**시스템 아키텍처**

```mermaid
flowchart TB
    subgraph Client["UI Layer"]
        Atelier["Atelier (React)"]
    end

    subgraph Server["Planner MCP Host"]
        subgraph API["API Layer"]
            FastAPI["FastAPI Server"]
            SSE["SSE Handler"]
            JSONRPC["JSON-RPC Handler"]
        end

        subgraph Core["Core Layer"]
            Orch["Orchestrator<br/>(세션/흐름 관리)"]
            Router["Intent Router<br/>(의도 분석)"]
            CtxMem["Context Memory<br/>(히스토리 관리)"]
            Compact["Context Compactor<br/>(자동 압축)"]
            Validator["Output Validator"]
        end

        subgraph Recipe["Recipe Layer"]
            DynGen["Dynamic Recipe<br/>Generator"]
            Executor["Recipe Executor"]
            SubRecipe["Sub-recipes<br/>(YAML)"]
        end

        subgraph Agent["Agent Layer"]
            StoryAg["Story Agent"]
            UXAg["UX Flow Agent"]
            IAAg["IA Agent"]
            PenpotAg["Penpot Agent"]
            DynAg["Dynamic Agent"]
        end
    end

    subgraph External["External"]
        LiteLLM["LiteLLM Provider"]
        MCPServers["MCP Servers"]
    end

    subgraph LLMProviders["LLM Providers"]
        OpenAI & Anthropic & Gemini & Ollama
    end

    Atelier <-->|HTTP/SSE| FastAPI
    FastAPI --> Orch
    Orch --> Router
    Router -->|의도 분석| LiteLLM
    Orch --> CtxMem
    CtxMem --> Compact
    
    Router -->|정적 Recipe| Executor
    Router -->|동적 Recipe| DynGen
    DynGen -->|Recipe 생성| LiteLLM
    DynGen --> SubRecipe
    
    Executor --> Agent
    Agent -->|산출물 생성| LiteLLM
    Agent --> Validator
    
    LiteLLM --> LLMProviders
    Executor -.->|Tool Call| MCPServers
```

**요청 처리 흐름 (정적 Recipe)**

```mermaid
sequenceDiagram
    actor User
    participant API as FastAPI
    participant Orch as Orchestrator
    participant Mem as Context Memory
    participant Router as Intent Router
    participant LLM1 as LiteLLM
    participant Exec as Recipe Executor
    participant Agent as Agent
    participant LLM2 as LiteLLM
    participant Valid as Validator

    User->>API: POST /process<br/>"로그인 기능 스토리 작성해줘"
    API->>Orch: process(session_id, user_input)
    
    Note over Orch,Mem: 1. 세션 관리
    Orch->>Mem: get_or_create_session()
    Mem-->>Orch: ContextMemory
    Orch->>Mem: add_message("user", input)
    
    Note over Orch,Router: 2. 의도 분석 (LLM 호출)
    Orch->>Router: route(user_input, context)
    Router->>LLM1: generate(system_prompt + recipes)
    LLM1-->>Router: {agent: "story", recipe: "create_story_ticket"}
    Router-->>Orch: RoutingResult
    
    Note over Orch,Exec: 3. Recipe 실행
    Orch->>Exec: execute(recipe, params)
    Exec->>Agent: execute(recipe, context)
    
    Note over Agent,LLM2: 4. 산출물 생성 (LLM 호출)
    Agent->>LLM2: generate(recipe_prompt)
    LLM2-->>Agent: 스토리 티켓 (Markdown)
    Agent-->>Exec: AgentOutput
    
    Note over Exec,Valid: 5. 검증 및 저장
    Exec->>Valid: validate(output)
    Exec->>Mem: add_artifact(result)
    Exec-->>Orch: 실행 결과
    
    Orch-->>API: ProcessResult
    API-->>User: SSE Stream 응답
```

**동적 Recipe 처리 흐름 (복합 요청)**

```mermaid
sequenceDiagram
    actor User
    participant Orch as Orchestrator
    participant Router as Intent Router
    participant DynGen as Dynamic Generator
    participant LLM as LiteLLM
    participant Exec as Recipe Executor
    participant Sub1 as Sub-recipe 1
    participant Sub2 as Sub-recipe 2

    User->>Orch: "쇼핑몰 로그인 기능 기획 전체 해줘"
    
    Note over Orch,Router: 1. 복합 요청 감지
    Orch->>Router: route(user_input)
    Router->>LLM: 의도 분석
    LLM-->>Router: use_dynamic_recipe: true
    
    Note over Orch,DynGen: 2. 동적 Recipe 생성
    Orch->>DynGen: generate(user_request)
    DynGen->>LLM: Sub-recipe 조합 계획
    LLM-->>DynGen: {sub_recipes: [story, userflow]}
    
    Note over Exec,Sub2: 3. 독립 세션에서 순차 실행
    DynGen->>Exec: execute_sub_recipes()
    Exec->>Sub1: create_story_ticket (독립 세션)
    Sub1-->>Exec: 스토리 티켓 결과
    Exec->>Sub2: create_userflow (독립 세션)
    Sub2-->>Exec: UX 플로우 결과
    
    Note over Orch: 4. 결과 통합
    Exec-->>Orch: 통합된 산출물
    Orch-->>User: 전체 기획 문서
```

**주요 기능**

[Core 시스템]
- Orchestrator: 전체 실행 흐름 조율, 세션 관리, Hook 이벤트 처리
- Intent Router: LLM 기반 사용자 의도 분석 → Agent/Recipe 자동 라우팅
- Context Memory: 세션별 대화 히스토리 및 산출물(Artifact) 저장
- Context Compactor: 토큰 한도 80% 도달 시 자동 요약 압축
- Output Validator: 산출물 스키마 검증 및 정리

[Recipe 시스템 - Goose 스타일]
- Dynamic Recipe Generator: 복합 요청 시 LLM이 Sub-recipe 조합 계획 수립
- Recipe Executor: YAML 기반 Recipe 실행, 독립 세션 Sub-recipe 지원
- Sub-recipe Tool: 각 Sub-recipe를 MCP Tool로 래핑하여 독립 실행

[Agent 시스템]
- story_agent: 스토리 티켓 작성 (배경, 목적, 인수조건 포함)
- uxflow_agent: UX 플로우차트 생성 (Mermaid.js 다이어그램)
- ia_agent: IA(정보 아키텍처) 설계 (사이트맵, 메뉴 트리)
- penpot_agent: Penpot 디자인 명세 생성
- dynamic_agent: 동적 Recipe 실행 (복합 산출물)
- general_agent: 일반 대화 및 챗봇 도움말 처리

[LLM 통합]
- LiteLLM Provider: 100+ LLM 프로바이더 단일 인터페이스
- 지원: OpenAI, Anthropic Claude, Google Gemini, Azure, Ollama 등
- models.yaml 별칭 시스템으로 쉬운 모델 전환
- Fallback 모델 자동 전환 (장애 대응)

**지원 산출물 (Sub-recipe)**

| 카테고리 | Sub-recipe | 설명 | 출력 형식 |
|----------|------------|------|-----------|
| Story | create_story_ticket | 스토리 티켓 작성 | Markdown |
| Story | refine_requirements | 요구사항 정제 | Markdown |
| UX Flow | create_userflow | 사용자 플로우 생성 | Mermaid.js |
| UX Flow | user_journey | 사용자 여정 맵 | Markdown |
| IA | sitemap | 사이트맵 설계 | JSON |
| IA | design_menu_tree | 메뉴 트리 설계 | JSON |
| Penpot | component_list | 컴포넌트 목록 | JSON |
| Penpot | create_design_spec | 디자인 명세 생성 | JSON |

**기술적 특징**

[MCP 프로토콜]
- SSE (Server-Sent Events) 기반 실시간 스트리밍
- JSON-RPC 2.0 프로토콜 통신
- 외부 MCP Server 연결 지원 (파일, DB, API 등)

[동적 Recipe 생성]
- Goose 스타일 Agentic 아키텍처
- 사용자 요청에 따라 Sub-recipe 자동 조합
- 독립 세션 실행으로 병렬 처리 가능

[컨텍스트 관리]
- ContextMemory: 대화 히스토리 + 산출물(Artifact) 통합 관리
- ContextCompactor: 토큰 한도 초과 방지 자동 압축
- HooksManager: 이벤트 기반 확장 지원

[템플릿 시스템]
- Jinja2 기반 산출물 템플릿
- story_ticket.md.j2, userflow.md.j2, design_spec.json.j2 등

**코드 구조**
```
mcp_host/
├── src/
│   ├── core/
│   │   ├── orchestrator.py      - 전체 실행 흐름 조율
│   │   ├── intent_router.py     - LLM 기반 의도 분석
│   │   ├── context_memory.py    - 세션/컨텍스트 관리
│   │   └── context_compaction.py - 자동 컨텍스트 압축
│   ├── agents/
│   │   ├── base_agent.py        - Agent 공통 인터페이스
│   │   ├── story_agent.py       - 스토리 티켓 생성
│   │   ├── uxflow_agent.py      - UX 플로우 생성
│   │   ├── ia_agent.py          - IA 설계
│   │   ├── penpot_agent.py      - 디자인 명세 생성
│   │   └── dynamic_agent.py     - 동적 Recipe 실행
│   ├── llm/
│   │   ├── provider.py          - LLM 추상화 레이어
│   │   └── litellm_provider.py  - LiteLLM 통합 (100+ 프로바이더)
│   ├── recipe/
│   │   ├── executor.py          - Recipe 실행 엔진
│   │   ├── dynamic_generator.py - 동적 Recipe 생성기
│   │   └── schema.py            - Recipe YAML 스키마
│   ├── server/
│   │   ├── main.py              - FastAPI 애플리케이션
│   │   ├── routes.py            - REST/SSE API 엔드포인트
│   │   └── sse_handler.py       - SSE 연결 관리
│   └── mcp_client/
│       └── sse_client.py        - 외부 MCP Server 연결
├── sub_recipes/                  - YAML 기반 Sub-recipe 정의
├── prompts/                      - Agent별 프롬프트 YAML
├── templates/                    - Jinja2 산출물 템플릿
└── config/
    ├── settings.yaml            - 서버/MCP 설정
    └── models.yaml              - LLM 모델 별칭 설정
```

**기술 스택**: Python, FastAPI, LiteLLM, Pydantic, Jinja2, YAML, SSE, JSON-RPC, MCP Protocol

---

## 프로젝트 타임라인

```
Phase 1: AI_LLM_API
|  - vLLM 기반 LLM 추론 엔진 구축
|  - 요약/분류/키워드 추출 API 개발
|  - LangGraph 에이전트 아키텍처 설계
|  - Gradio UI 개발
|
Phase 2: RAG 시스템 (AI_PROMPT + RAG-Chatbot)
|  - Milvus 벡터 DB 설계 및 구축
|  - 하이브리드 검색 시스템 개발 (Dense + BM25)
|  - Reranking 파이프라인 구현
|  - Agentic RAG 아키텍처 설계
|  - LlamaGuard 안전성 검증 통합
|  - Streamlit 챗봇 UI 개발
|
Phase 3: 서울 상권분석 시스템 (sbiz_db + sbiz_llm)
|  - PostgreSQL 스키마 설계 (9개 테이블)
|  - 서울 Open API 데이터 파이프라인 구축
|  - 상권분석 LLM Agent 개발
|  - Tool Calling 기반 DB 검색 구현
|  - FastAPI 백엔드 구현
|
Phase 4: Planner MCP Host
   - MCP 프로토콜 기반 Host 아키텍처 설계
   - LiteLLM 통합 (100+ LLM 프로바이더 지원)
   - Goose 스타일 동적 Recipe 시스템 구현
   - Intent Router 기반 의도 분석 및 Agent 라우팅
   - 기획 산출물 자동 생성 Agent 개발 (Story, UX Flow, IA, Penpot)
   - 컨텍스트 자동 압축 시스템 구현
   - FastAPI + SSE 실시간 스트리밍 서버 구현
```

---

## 연락처

- 이메일:cyon13022@gmail.com

