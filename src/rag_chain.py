import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from src.retriever import retrieve_documents

load_dotenv()


def get_llm():

    api_key=st.secrets.get(
        "GROQ_API_KEY",
        os.getenv("GROQ_API_KEY")
    )

    if not api_key:
        raise ValueError(
            "Missing GROQ_API_KEY"
        )

    llm=ChatGroq(
        groq_api_key=api_key,
        model_name="llama3-8b-8192"
    )

    return llm


def answer_question(query):

    docs=retrieve_documents(query)

    context="\n".join(
        [d.page_content for d in docs]
    )

    prompt=f"""
Use ONLY the context below.

Context:
{context}

Question:
{query}

Answer clearly:
"""

    llm=get_llm()

    response=llm.invoke(prompt)

    return (
        response.content,
        docs,
        [d.page_content for d in docs]
    )
