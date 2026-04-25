import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from src.retriever import retrieve_documents

load_dotenv()


def get_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")

    return ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )


def answer_question(query):
    docs = retrieve_documents(query)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Use the context below to answer.

Context:
{context}

Question:
{query}
"""

    llm = get_llm()
    response = llm.invoke(prompt)

    return response.content, docs, docs