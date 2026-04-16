import re


def chunk_text(text, chunk_size=500, overlap=100):
    if not text:
        return []

    text = re.sub(r"\n{2,}", "\n\n", text.strip())
    chunks = []
    start = 0
    text_len = len(text)

    while start < text_len:
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= text_len:
            break

        start += chunk_size - overlap

    return chunks


def bronze_to_silver_chunks(spark, source_table: str, target_table: str):
    from pyspark.sql import Row

    docs = (
        spark.table(source_table)
        .select("doc_id", "doc_title", "file_name", "source_path", "content_raw", "ingest_time")
        .collect()
    )

    chunk_rows = []
    for d in docs:
        chunks = chunk_text(d["content_raw"], chunk_size=500, overlap=100)

        for i, c in enumerate(chunks):
            chunk_rows.append(
                Row(
                    chunk_id=f"{d['doc_id']}_{i}",
                    doc_id=d["doc_id"],
                    doc_title=d["doc_title"],
                    file_name=d["file_name"],
                    source_path=d["source_path"],
                    chunk_order=i,
                    chunk_text=c,
                    ingest_time=d["ingest_time"],
                )
            )

    chunk_df = spark.createDataFrame(chunk_rows)

    (
        chunk_df.write.format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .saveAsTable(target_table)
    )
