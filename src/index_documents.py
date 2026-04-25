from src.loaders import load_documents
from src.chunking import chunk_documents
from src.embeddings import get_embedding_model
from src.config import DATA_PATH, DB_PATH

from langchain_community.vectorstores import FAISS


def create_index():

    print("Loading documents...")
    docs = load_documents(DATA_PATH)

    print(f"Loaded {len(docs)} pages")

    print("Chunking documents...")
    chunks = chunk_documents(docs)

    print(f"Created {len(chunks)} chunks")

    print("Building embeddings and FAISS index...")

    embeddings = get_embedding_model()

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    db.save_local(DB_PATH)

    print("Index created successfully!")


if __name__=="__main__":
    create_index()