import os
from langchain_community.vectorstores import FAISS
from src.embeddings import get_embedding_model
from src.loaders import load_documents
from src.chunking import chunk_documents
from src.config import DB_PATH, DATA_PATH, TOP_K

def retrieve_documents(query):
    embeddings = get_embedding_model()

    # Build index if missing
    if not os.path.exists(DB_PATH):
        docs = load_documents(DATA_PATH)
        chunks = chunk_documents(docs)

        db = FAISS.from_documents(
            chunks,
            embeddings
        )
        db.save_local(DB_PATH)

    db = FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db.similarity_search(query, k=TOP_K)
