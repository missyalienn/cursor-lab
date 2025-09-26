# Implementation Plan
## Workbench DIY Project Companion

**Goal**: Zero-cost functional MVP with core features

---

## Phase 1: Reddit Auth & Data Pipeline

### Step 1.1: Environment Setup
- [x] Initialize project structure per AGENTS.md guidelines
- [x] Create `.env.` and `.gitignore` (exclude .env)
- [x] Create `requirements.txt` with dependencies 

### Step 1.2: Reddit API Data Ingestion
- [x] Authenticate to Reddit API 
- [x] Generate Reddit client ID and secret, store in keychain
- [x] Test Reddit API authentication and confirm working
- [x] Generate top 10 posts from r/diy as test
- [x] Fetch top 10 posts from r/diy last month and top 5 comments per post
- [x] JSON storage for raw data
- [] Clean and normalize post and comment text (remove markdown, URLs, extra whitespace) 

### Step 1.3: Vector Pipeline
- [ ] Sentence Transformers setup
- [ ] Text embedding generation
- [ ] Pinecone client configuration
- [ ] Initial vector upload script
- [ ] Test with sample data

**Deliverables**: Working data pipeline, initial vector store

---

## Phase 2: Search API & RAG System

### Step 2.1: Search Service
- [ ] Semantic search implementation
- [ ] Query preprocessing
- [ ] Result ranking and filtering
- [ ] Core search module setup

### Step 2.2: RAG Response System
- [ ] Format search results for display
- [ ] Source citation formatting
- [ ] Response structure design
- [ ] Basic error handling
- [ ] Performance optimization

**Deliverables**: Working RAG system with semantic search

---

## Phase 3: CLI & LLM Integration

### Step 3.1: CLI Interface
- [ ] Simple command-line interface
- [ ] Question input and response display
- [ ] Source citation output
- [ ] Basic usage monitoring

### Step 3.2: LLM Enhancement Layer
- [ ] OpenAI API integration
- [ ] Context preparation from search results
- [ ] Response formatting with citations
- [ ] Token counting and cost controls
- [ ] Toggle between RAG/RAG+LLM modes

**Deliverables**: Working CLI demo with optional LLM enhancement

---

## Implementation Details

### File Structure
```
/workbench/
├── config/
│   └── settings.py          # Environment configuration from .env
├── scripts/
│   ├── reddit_ingester.py   # Reddit data fetching
│   └── vector_updater.py    # Vector store updates
├── src/
│   ├── search/
│   │   ├── semantic_search.py   # Core search logic
│   │   └── query_processor.py   # Query preprocessing
│   ├── rag/
│   │   ├── response_formatter.py # RAG response formatting
│   │   └── source_handler.py    # Source citation management
│   ├── llm/ (Phase 2)
│   │   ├── context_builder.py   # Context preparation
│   │   ├── openai_client.py     # OpenAI API client
│   │   └── enhancement.py       # LLM response enhancement
│   └── cli/
│       └── main.py              # CLI application
├── cli-demo.py              # CLI demo application
├── docs/                    # Documentation
├── .env.example             # Environment template
├── .gitignore               # Exclude .env and sensitive files
└── requirements.txt         # Dependencies
```

### Key Dependencies
```
# Core
sentence-transformers
pinecone-client  # Free tier only
openai  # Local simulation
praw  # Reddit API

# Data & Utils
pandas
python-dotenv
pytest
requests
```

### Phase Checkpoints
- **Phase 1**: Data pipeline functional test
- **Phase 2**: Search returning results
- **Phase 3**: RAG system working
- **Phase 4**: LLM integration complete
- **Final**: Complete zero-cost demo

### Risk Mitigation
- **API Rate Limits**: Implement caching and throttling
- **Vector Store Issues**: Local vector storage for development
- **Zero Cost Requirement**: Local-only implementation option
- **Time Constraints**: Extended timeline for thorough testing

---

## Documentation Plan

### Core Component Docs (Created by Phase)

**Phase 1**:
- `reddit_data_pipeline.md`
- `vector_storage_setup.md`

**Phase 2**:
- `search_api_reference.md`
- `rag_system_guide.md`

**Phase 3**:
- `llm_integration_guide.md`
- `cli_usage_guide.md`
- `deployment_instructions.md`

### Documentation Template
Each doc includes:
- **Purpose**: What the component does
- **Configuration**: Required settings
- **API Reference**: Functions and endpoints
- **Examples**: Usage code samples
- **Troubleshooting**: Common issues

---

## Success Criteria
- [ ] Users can ask DIY questions and get relevant answers
- [ ] Semantic search returns relevant Reddit r/diy content
- [ ] AI generates helpful responses with source citations
- [ ] OpenAI integration works reliably
- [ ] Cost controls prevent budget overrun
- [ ] System handles 50+ concurrent queries
- [ ] All core components documented
