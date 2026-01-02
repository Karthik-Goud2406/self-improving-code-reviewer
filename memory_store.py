from typing import List

try:
    from langchain_chroma import Chroma
    from langchain_openai import OpenAIEmbeddings
    EMBEDDINGS_AVAILABLE = True
except Exception:
    EMBEDDINGS_AVAILABLE = False

_db = None

def _init_db():
    global _db
    if not EMBEDDINGS_AVAILABLE:
        return None
    if _db is None:
        embedding = OpenAIEmbeddings()
        _db = Chroma(
            persist_directory="./memory",
            embedding_function=embedding
        )
    return _db

def retrieve_memory(context) -> List[str]:
    db = _init_db()
    if not db:
        return []  # graceful fallback

    try:
        results = db.similarity_search(context["diff"], k=2)
        return [r.page_content for r in results]
    except Exception:
        return []

def store_feedback(context, feedback):
    db = _init_db()
    if not db:
        return
    try:
        db.add_texts([feedback])
    except Exception:
        pass
