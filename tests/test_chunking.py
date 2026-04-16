from src.chunking import chunk_text


def test_chunk_text_basic():
    text = "A" * 1200
    chunks = chunk_text(text, chunk_size=500, overlap=100)
    assert len(chunks) >= 2
    assert all(len(c) > 0 for c in chunks)
