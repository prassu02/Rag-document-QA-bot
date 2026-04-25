import streamlit as st
from src.rag_chain import answer_question

st.title("RAG Document Q&A Bot")

query = st.text_input("Ask a question from documents")

if query:
    with st.spinner("Searching documents..."):
        answer, sources, chunks = answer_question(query)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Sources")

    seen = set()

    for s in sources:
        src = f"{s.metadata['source']} | Page {s.metadata['page']}"
        if src not in seen:
            st.write(src)
            seen.add(src)

    st.subheader("Retrieved Chunks")

    for i, chunk in enumerate(chunks,1):
        st.write(f"Chunk {i}")
        st.write(chunk.page_content[:500])
        st.write("---")