# Resume / GitHub Project One-Liner

## English
Built a Databricks-based enterprise asset knowledge RAG platform that transforms internal documents into governed, searchable, and LLM-ready knowledge services for high-governance industries.

## 中文
建立以 Databricks 為基礎的企業資產知識庫 LLM RAG 平台，將內部文件轉成可治理、可搜尋、可供 AI 使用的知識服務，適用於高治理需求產業。

# 面試 30 秒說法
我做的不是單純文件 chatbot，而是一個建構在 Databricks Data Platform 上的企業資產知識庫 LLM RAG 平台。它能把分散在 Word 與文件系統中的內部知識，轉成可治理、可搜尋、可供 LLM 問答的知識服務，這種模式可延伸到半導體 SOP、金融治理文件、incident 知識與資料字典等場景。

# 面試 90 秒說法
很多企業的重要知識都散落在 Word 文件、操作文件、規範、歷史專案資料與各種內部文檔中。這些內容很難搜尋、很難 onboarding，也常依賴特定人的經驗記憶。我在 Databricks 上做了一套企業資產知識庫 LLM RAG 平台，先把文件抽出文字寫進 Delta tables，再做 chunking，建立 Vector Search index，最後接上 Databricks LLM 做 grounded answering。這樣的重點不是做一個聊天機器人，而是把企業文件正式轉成可治理、可被 AI 使用的知識層。這套模式可以複用到 SOP、風控規則、incident postmortem、資料表定義與架構文件，在半導體與金融這類高治理產業尤其有價值。
