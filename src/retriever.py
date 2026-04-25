import os
from langchain_community.vectorstores import FAISS
from src.embeddings import get_embedding_model
from src.loaders import load_documents

DB_PATH="faiss_index"

def retrieve_documents(query):
    embeddings = get_embedding_model()

    try:
        if os.path.exists(DB_PATH):
            db = FAISS.load_local(
                DB_PATH,
                embeddings,
                allow_dangerous_deserialization=True
            )
        else:
            docs = load_documents()
            db = FAISS.from_documents(docs, embeddings)
            db.save_local(DB_PATH)

        return db.similarity_search(query,k=4)

    except Exception as e:
        print("ERROR:", e)
        raise e
