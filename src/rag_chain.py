import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from src.retriever import retrieve_documents

load_dotenv()

def get_llm():

    api_key = st.secrets["GROQ_API_KEY"]

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