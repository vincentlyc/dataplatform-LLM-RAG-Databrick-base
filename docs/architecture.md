# Architecture Overview

## Objective
Build an enterprise-grade knowledge retrieval and grounded question-answering platform using Databricks-native components.

## Architecture Goal
Transform internal documents into a governed knowledge service that can be searched, retrieved, and used by LLM applications.

## End-to-End Flow
1. Enterprise Word documents are uploaded into a controlled storage path.
2. Python extracts text from `.docx` files.
3. Raw document content is stored in a Bronze Delta table.
4. Documents are chunked into searchable knowledge units and stored in a Silver Delta table.
5. Databricks Vector Search index is built on the Silver table.
6. User questions query the vector index to retrieve top-K relevant knowledge chunks.
7. Retrieved chunks are passed to a Databricks-hosted LLM for grounded answer generation.
8. Token usage and estimated cost are recorded for visibility.

## Core Design Decisions
- Use Databricks-native Delta + Vector Search instead of external vector DB to align with enterprise governance
- Use metadata columns (`doc_id`, `doc_title`, `chunk_order`) for source traceability
- Use pay-per-token LLM to accelerate PoC and improve cost visibility
- Keep ingestion, chunking, retrieval, and generation modular for maintainability

## Why this architecture matters
- Enables knowledge assets to become AI-ready
- Reduces document search and onboarding friction
- Creates a reusable pattern for SOP, governance documents, architecture documents, incident reports, and internal knowledge bases
- Bridges the data platform and AI application layer

## Data Layers
### Bronze
Raw document ingestion layer

### Silver
Cleaned and chunked knowledge units for semantic retrieval

### Vector Search Layer
Semantic index built on top of Silver knowledge chunks

### LLM Layer
Grounded answer generation based on retrieved enterprise knowledge

## Recommended Future Enhancements
- support PDF and markdown
- add metadata filters
- support incremental sync
- add feedback logging
- connect to app layer (Streamlit / Databricks App)
- implement document-level access control
