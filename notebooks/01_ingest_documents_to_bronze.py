from src.config import BRONZE_TABLE
from src.ingest_documents import ingest_docx_folder_to_bronze

ingest_docx_folder_to_bronze(
    spark=spark,
    base_path="/Volumes/dev/bronze/enterprise_docs/word",
    target_table=BRONZE_TABLE,
)

print(f"Loaded enterprise documents into {BRONZE_TABLE}")
