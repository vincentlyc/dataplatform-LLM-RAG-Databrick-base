from databricks_openai import DatabricksOpenAI


class EnterpriseKnowledgeAnswerGenerator:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.client = DatabricksOpenAI()

    def generate(self, question: str, context: str) -> dict:
        system_prompt = """
你是一個企業知識庫問答助手。
請只根據提供的企業文件內容回答。
如果提供內容不足，請明確回答：
「根據目前檢索到的企業知識內容，無法確定。」
不要自行腦補不存在的制度、政策、規範或決策。
回答請使用繁體中文。
最後請列出引用到的 doc_title。
"""

        user_prompt = f"""
以下是從企業知識向量檢索回來的內容：

{context}

使用者問題：
{question}

請輸出：
1. 直接回答問題
2. 若有多份文件相關，整理差異
3. 最後列出引用到的 doc_title
"""

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.1,
            max_tokens=800,
        )

        usage = getattr(response, "usage", None)
        input_tokens = getattr(usage, "prompt_tokens", None) if usage else None
        output_tokens = getattr(usage, "completion_tokens", None) if usage else None
        total_tokens = getattr(usage, "total_tokens", None) if usage else None

        return {
            "answer": response.choices[0].message.content,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
        }
