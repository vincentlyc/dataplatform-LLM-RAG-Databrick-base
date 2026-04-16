from src.vector_retrieval import build_context


def test_build_context():
    rows = [
        {
            "doc_id": "DOC-001",
            "doc_title": "Test Knowledge Document",
            "chunk_order": 0,
            "chunk_text": "This is a chunk.",
        }
    ]

    context = build_context(rows)
    assert "DOC-001" in context
    assert "Test Knowledge Document" in context
    assert "This is a chunk." in context
