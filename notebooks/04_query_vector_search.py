from src.config import VECTOR_ENDPOINT, VECTOR_INDEX
from src.vector_retrieval import EnterpriseKnowledgeRetriever, parse_search_results

retriever = EnterpriseKnowledgeRetriever(VECTOR_ENDPOINT, VECTOR_INDEX)
results = retriever.similarity_search("incremental load 時間欄位統一規範", num_results=3)
rows = parse_search_results(results)

for row in rows:
    print(row)
