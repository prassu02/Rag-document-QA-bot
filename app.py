import streamlit as st
from src.rag_chain import answer_question

st.set_page_config(
    page_title="RAG Document Q&A Bot",
    layout="wide"
)

st.title("📄 RAG Document Q&A Bot")
st.write("Ask questions from your uploaded document corpus")

query = st.text_input(
    "Ask a question",
    placeholder="What is machine learning?"
)

if query:
    with st.spinner("Searching documents..."):
        try:
            answer, sources, chunks = answer_question(query)

            st.subheader("Answer")
            st.write(answer)

            with st.expander("Retrieved Chunks"):
                for i,c in enumerate(chunks,1):
                    st.write(f"Chunk {i}")
                    st.write(c)
                    st.divider()

        except Exception as e:
            st.error(f"Error: {str(e)}")
