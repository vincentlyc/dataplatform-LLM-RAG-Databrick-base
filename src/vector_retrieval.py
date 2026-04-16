class EnterpriseKnowledgeRetriever:
    def __init__(self, endpoint_name: str, index_name: str):
        from databricks.vector_search.client import VectorSearchClient

        self.client = VectorSearchClient(disable_notice=True)
        self.index = self.client.get_index(
            endpoint_name=endpoint_name,
            index_name=index_name,
        )

    def similarity_search(self, query: str, num_results: int = 4):
        return self.index.similarity_search(
            query_text=query,
            columns=["chunk_id", "doc_id", "doc_title", "chunk_order", "chunk_text"],
            num_results=num_results,
        )


def parse_search_results(search_results: dict):
    manifest = search_results.get("manifest", {})
    data_array = search_results.get("result", {}).get("data_array", [])
    columns = [c["name"] for c in manifest.get("columns", [])]
    return [dict(zip(columns, row)) for row in data_array]


def build_context(rows: list) -> str:
    if not rows:
        return "沒有找到相關企業知識內容。"

    parts = []
    for r in rows:
        parts.append(
            f"[doc_id] {r.get('doc_id', '')}\n"
            f"[doc_title] {r.get('doc_title', '')}\n"
            f"[chunk_order] {r.get('chunk_order', '')}\n"
            f"[chunk_text]\n{r.get('chunk_text', '')}"
        )

    return "\n\n---\n\n".join(parts)
