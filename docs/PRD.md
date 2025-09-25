# Product Requirements Document (PRD)
## Workbench - DIY Project Companion

### Overview
Workbench is an AI-powered DIY project companion that helps users find relevant information, tips, and solutions from the Reddit DIY community using semantic search and optional AI assistance.

### Core Objectives
- **Phase 1**: Build semantic search RAG for Reddit r/diy content
- **Phase 2**: Add LLM enhancement once search is proven
- **Ongoing**: Minimize API costs through intelligent usage controls

---

## Technical Architecture

### Data Pipeline
| Component | Technology | Purpose |
|-----------|------------|---------|
| **Data Source** | Reddit API (r/diy) | Fetch posts, comments, project data |
| **Embeddings** | Sentence Transformers | Convert text to vectors |
| **Vector Store** | Pinecone | Store and search embeddings |
| **LLM Integration** | OpenAI API | AI response generation |

### Core Features

#### 1. Semantic Search Engine
- **Input**: User queries about DIY projects
- **Process**: Vector similarity search in Pinecone
- **Output**: Ranked relevant Reddit posts/comments

#### 2. Response System (Phased)
- **Phase 1**: Semantic search → Formatted results with source links
- **Phase 2**: Add LLM layer for enhanced responses
- **Controls**: 
  - Token limits and cost monitoring (Phase 2)
  - Request queuing and rate limiting
  - Error handling and graceful degradation

#### 3. Data Management
- **Reddit Ingestion**: Scheduled data fetching
- **Vector Updates**: Incremental embedding updates
- **Storage Optimization**: Efficient vector indexing

---

## User Experience

### Primary Use Cases
1. **Quick Search**: Find relevant DIY solutions instantly
2. **Project Planning**: Get comprehensive project guidance
3. **Troubleshooting**: Find solutions to specific problems

### User Flow
```
Phase 1: User Query → Semantic Search → Ranked Results + Sources
Phase 2: User Query → Semantic Search → Context → LLM → AI Response + Sources
```

### Interface Requirements
- Clean, minimal search interface
- AI-generated responses with clear source attribution
- Reddit source links for verification
- Usage/cost monitoring dashboard

---

## Non-Functional Requirements

### Performance
- Search response time: < 2 seconds
- Vector search accuracy: > 85% relevance
- System uptime: > 99%

### Cost Control
- OpenAI API: Configurable daily limits
- Pinecone: Optimized query patterns
- Reddit API: Respect rate limits

### Modularity
- Separate data ingestion pipeline
- Independent search service
- Optional AI enhancement layer
- Configurable components

---

## Success Metrics
- **Search Quality**: User satisfaction with results
- **Cost Efficiency**: Stay within budget limits
- **Performance**: Sub-2s response times
- **Usage**: Daily active searches

---

## Documentation Requirements
Each core component must have:
- Purpose and functionality
- API/interface specifications
- Usage examples
- Troubleshooting guide

Saved in `/docs` folder with clear naming convention.
