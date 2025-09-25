# 5-Day Implementation Plan
## Workbench DIY Project Companion

**Timeline**: Thursday - Tuesday  
**Goal**: Zero-cost functional MVP with core features

---

## Day 1 (Thursday) - Foundation & Data Pipeline

### Morning (4 hours)
- **Project Setup**
  - [x] Initialize project structure per AGENTS.md guidelines
  - [x] Create `.env.` and `.gitignore` (exclude .env)
  - [x] Create `requirements.txt` with dependencies 
  

- **Reddit Data Ingestion**
  - [x] Authenticate to Reddit API 
  - [x] Generate Reddit client ID and secret, store in keychain
  - [x] Test Reddit API authentication and confirm working
  - [x] Generate top 10 posts from r/diy as test
  - [ ] Fetch top r/diy posts from last year only
  - [ ] Data cleaning and preprocessing
  - [ ] JSON storage for raw data

### Afternoon (4 hours)
- **Vector Pipeline**
  - [ ] Sentence Transformers setup
  - [ ] Text embedding generation
  - [ ] Pinecone client configuration
  - [ ] Initial vector upload script
  - [ ] Test with sample data

**Deliverables**: Working data pipeline, initial vector store

---

## Day 2 (Friday) - Search API & RAG System

### Morning (4 hours)
- **Search Service**
  - [ ] Semantic search implementation
  - [ ] Query preprocessing
  - [ ] Result ranking and filtering
  - [ ] Core search module setup

### Afternoon (4 hours)
- **RAG Response System**
  - [ ] Format search results for display
  - [ ] Source citation formatting
  - [ ] Response structure design
  - [ ] Basic error handling
  - [ ] Performance optimization

**Deliverables**: Working RAG system with semantic search

---

## Day 3 (Monday) - CLI & LLM Integration

### Morning (4 hours)
- **CLI Interface**
  - [ ] Simple command-line interface
  - [ ] Question input and response display
  - [ ] Source citation output
  - [ ] Basic usage monitoring

### Afternoon (4 hours)
- **LLM Enhancement Layer**
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

### Daily Checkpoints
- **Day 1 (Thursday)**: Data pipeline functional test
- **Day 2 (Friday)**: Search returning results
- **Day 3 (Monday)**: RAG system working
- **Day 4 (Tuesday)**: LLM integration complete
- **Day 5 (Wednesday)**: Complete zero-cost demo

### Risk Mitigation
- **API Rate Limits**: Implement caching and throttling
- **Vector Store Issues**: Local vector storage for development
- **Zero Cost Requirement**: Local-only implementation option
- **Time Constraints**: Extended timeline for thorough testing

---

## Documentation Plan

### Core Component Docs (Created Daily)

**Day 1 (Thursday)**:
- `reddit_data_pipeline.md`
- `vector_storage_setup.md`

**Day 2 (Friday)**:
- `search_api_reference.md`
- `rag_system_guide.md`

**Day 3 (Monday)**:
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
