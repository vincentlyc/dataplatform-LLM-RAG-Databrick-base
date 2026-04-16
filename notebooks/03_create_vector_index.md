# Create Vector Search Index

## Source table
`dev.silver.enterprise_knowledge_chunks`

## Recommended settings
- Primary key: `chunk_id`
- Columns to index:
  - `chunk_id`
  - `chunk_text`
  - `doc_id`
  - `doc_title`
  - `chunk_order`
- Index subtype: `Hybrid Index`
- Embedding source: `Compute embeddings`
- Embedding source column: `chunk_text`
- Embedding model: `databricks-qwen3-embedding-0-6b`
- Vector Search endpoint: `pymt-vector-endpoint`
- Sync mode: `Triggered`

## Prerequisite
```sql
ALTER TABLE dev.silver.enterprise_knowledge_chunks
SET TBLPROPERTIES (delta.enableChangeDataFeed = true);
```
