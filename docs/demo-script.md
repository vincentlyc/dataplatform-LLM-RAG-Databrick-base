# Demo Script

## 30-Second Version
I built a Databricks-based enterprise asset knowledge RAG platform that transforms internal documents into a governed, searchable, and LLM-ready knowledge service. It helps teams retrieve internal knowledge faster and get grounded answers based on enterprise documents instead of model guesswork.

## 90-Second Version
Many enterprises store critical knowledge in Word files, operational documents, governance files, and historical project records. These documents are usually difficult to search, difficult to reuse, and heavily dependent on tribal knowledge.

I built a Databricks-native workflow that extracts text from internal documents, stores them in Delta tables, chunks them into searchable knowledge units, builds a Vector Search index, and then uses a Databricks-hosted LLM to generate grounded answers based on retrieved content.

This is not just a chatbot. It is an enterprise knowledge service layer that can be extended to SOPs, governance standards, incident records, architecture files, and table definitions.

## Demo Questions
- Which document defines the incremental load time field standard?
- What is the update strategy for unique key mapping in withdrawal data?
- What is the logic behind CPS Status 7?
- Which internal documents are related to data update strategies?

## Closing Statement
This project demonstrates how internal files can be transformed into a governed enterprise AI knowledge platform on Databricks, which is especially relevant for high-governance industries such as semiconductor and financial services.
