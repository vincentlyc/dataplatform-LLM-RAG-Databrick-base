# Enterprise Asset Knowledge RAG on Databricks

A Databricks-based enterprise asset knowledge platform that transforms internal documents into governed, searchable, and LLM-ready knowledge services.

## Project Summary
This project demonstrates how to transform enterprise internal knowledge documents from static Word files into a governed, searchable, and AI-ready knowledge platform using Databricks Vector Search and LLM.

## Why this project matters
In many enterprises, critical knowledge is locked inside Word documents, SOPs, operational records, governance files, architecture documents, historical project materials, and internal standards.

These assets are often:
- hard to search
- difficult to reuse
- dependent on tribal knowledge
- inefficient for onboarding
- slow for cross-functional collaboration

This project converts those files into an enterprise knowledge retrieval and question-answering platform.

## Business Value
- Reduce time spent searching internal knowledge documents
- Improve onboarding efficiency for engineers and business teams
- Convert static files into reusable enterprise knowledge assets
- Provide grounded AI answers based on internal documentation instead of model guesswork
- Extend the data platform into an enterprise AI knowledge service layer

## Target Industries
### Semiconductor
- SOPs
- process standards
- equipment maintenance documents
- yield / defect analysis knowledge
- engineering change records

### Financial Services
- governance documents
- payment / settlement procedures
- risk control documentation
- compliance / regulatory interpretation documents
- data lineage and incident knowledge

### General Enterprise / IT
- internal standards
- architecture documents
- postmortem files
- table definitions
- operational handbooks
- knowledge base files

## Architecture
```text
Enterprise Knowledge Documents (Word / Docs / Files)
   ↓
Text Extraction
   ↓
Bronze Delta Table
   ↓
Chunking / Cleaning
   ↓
Silver Knowledge Chunk Table
   ↓
Databricks Vector Search Index
   ↓
Retrieve Top-K Relevant Knowledge Chunks
   ↓
Databricks LLM (pay-per-token)
   ↓
Enterprise Knowledge Assistant
```

## Key Highlights
- Word document ingestion
- Databricks Delta-based document pipeline
- Semantic chunking for knowledge retrieval
- Vector Search-based enterprise knowledge retrieval
- Grounded LLM question answering
- Token usage and cost estimation
- Metadata-based traceability

## Tech Stack
- Databricks
- Delta Lake
- Unity Catalog
- Databricks Vector Search
- Databricks Foundation Model APIs
- Python
- python-docx
- RAG (Retrieval-Augmented Generation)

## Repository Structure
```text
enterprise-asset-knowledge-rag-databricks/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ requirements.txt
├─ docs/
│  ├─ architecture.md
│  ├─ business-value.md
│  ├─ demo-script.md
│  └─ screenshots/
├─ notebooks/
│  ├─ 01_ingest_documents_to_bronze.py
│  ├─ 02_chunk_bronze_to_silver.py
│  ├─ 03_create_vector_index.md
│  ├─ 04_query_vector_search.py
│  ├─ 05_enterprise_knowledge_rag_assistant.py
│  └─ 06_token_cost_estimation.py
├─ src/
│  ├─ config.py
│  ├─ ingest_documents.py
│  ├─ chunking.py
│  ├─ vector_retrieval.py
│  ├─ llm_answering.py
│  └─ cost_utils.py
├─ data_samples/
│  └─ sample_documents/
├─ tests/
│  ├─ test_chunking.py
│  └─ test_context_builder.py
└─ assets/
   ├─ architecture-diagram.png
   └─ demo-output.png
```

## Quick Start
1. Upload enterprise knowledge `.docx` files to a Databricks Volume or workspace path
2. Run document ingestion notebook
3. Run chunking notebook
4. Create Vector Search endpoint and index
5. Run semantic retrieval
6. Run enterprise knowledge RAG assistant
7. Observe token usage and estimated LLM cost

## Example Questions
- Which document defines the incremental load time field standard?
- What is the update strategy for unique key mapping in withdrawal data?
- What is the logic behind CPS Status 7?
- What is the onboarding scope of the fund table data source?
- Which internal documents explain data update strategies?

## Why this project is valuable for enterprise hiring
This is not just a chatbot demo. It demonstrates:
- enterprise data platform thinking
- LLM + vector retrieval implementation
- knowledge asset transformation
- AI governance awareness
- cost visibility
- cross-functional communication capability

## Career Positioning
This project is designed to demonstrate enterprise AI platform capability for semiconductor, financial services, and large-scale data platform leadership roles.

## License
MIT
