from src.config import VECTOR_ENDPOINT, VECTOR_INDEX, CHAT_MODEL, TOP_K
from src.vector_retrieval import EnterpriseKnowledgeRetriever, parse_search_results, build_context
from src.llm_answering import EnterpriseKnowledgeAnswerGenerator
from src.cost_utils import estimate_gpt54_global_short_dbu

retriever = EnterpriseKnowledgeRetriever(VECTOR_ENDPOINT, VECTOR_INDEX)
answerer = EnterpriseKnowledgeAnswerGenerator(CHAT_MODEL)


def ask_enterprise_knowledge_assistant(question: str, num_results: int = TOP_K):
    search_results = retriever.similarity_search(question, num_results=num_results)
    rows = parse_search_results(search_results)
    context = build_context(rows)
    llm_result = answerer.generate(question, context)

    if llm_result["input_tokens"] is not None and llm_result["output_tokens"] is not None:
        cost = estimate_gpt54_global_short_dbu(
            llm_result["input_tokens"],
            llm_result["output_tokens"],
        )
    else:
        cost = None

    return {
        "question": question,
        "retrieved_rows": rows,
        "context": context,
        "answer": llm_result["answer"],
        "input_tokens": llm_result["input_tokens"],
        "output_tokens": llm_result["output_tokens"],
        "total_tokens": llm_result["total_tokens"],
        "cost": cost,
    }


result = ask_enterprise_knowledge_assistant("哪份文件在談 incremental load 時間欄位統一規範？")
print(result["answer"])
print(result["cost"])
