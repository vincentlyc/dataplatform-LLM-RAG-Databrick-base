from src.config import BRONZE_TABLE, SILVER_TABLE
from src.chunking import bronze_to_silver_chunks

bronze_to_silver_chunks(
    spark=spark,
    source_table=BRONZE_TABLE,
    target_table=SILVER_TABLE,
)

print(f"Chunked documents into {SILVER_TABLE}")
