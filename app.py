import streamlit as st
from ingest import load_documents
from utils import chunk_text
from vectorstore import VectorStore
from rag_pipeline import get_embedding, generate_answer
from reranker import rerank
from retrieval_utils import keyword_filter

st.title("📄 RAG Document Q&A Bot (Groq + FAISS)")


# -----------------------------
# BUILD VECTOR INDEX
# -----------------------------
@st.cache_resource
def build_index():
    docs = load_documents("data")

    store = VectorStore()

    all_chunks = []
    all_embeddings = []

    for doc in docs:
        filename = doc["filename"]
        text = doc["text"]

        # ✅ CREATE CHUNKS (FIX)
        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            all_chunks.append(f"{filename} | Chunk {i}: {chunk}")
            all_embeddings.append(get_embedding(chunk))

    store.add(all_embeddings, all_chunks)

    return store


store = build_index()


# -----------------------------
# USER QUERY
# -----------------------------
query = st.text_input("Ask a question:")

if query:

    # Step 1: Embed query
    q_emb = get_embedding(query)

    # Step 2: Retrieve from FAISS
    retrieved = store.search(q_emb, k=10)

    # Safety check
    if not retrieved:
        st.warning("No relevant documents found.")
        st.stop()

    # Step 3: Keyword filtering
    retrieved = keyword_filter(query, retrieved)

    # Step 4: Reranking (Cross-encoder)
    retrieved = rerank(query, retrieved)

    # Step 5: Final top-k selection
    retrieved = retrieved[:3]

    # Safety check after ranking
    if not retrieved:
        st.warning("No strong matches after reranking.")
        st.stop()

    # Step 6: Generate answer
    answer = generate_answer(query, retrieved)

    # -----------------------------
    # OUTPUT
    # -----------------------------
    st.subheader("Answer")
    st.write(answer)

    st.subheader("Retrieved Chunks")
    for r in retrieved:
        st.write(r)