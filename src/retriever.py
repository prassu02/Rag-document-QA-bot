from langchain_community.vectorstores import FAISS
from src.embeddings import get_embedding_model
from src.config import DB_PATH,TOP_K

def retrieve_documents(query):

    embeddings=get_embedding_model()

    db=FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs=db.similarity_search(
        query,
        k=TOP_K
    )

    return docs