import os
import streamlit as st
from src.rag_chain import get_llm

def get_llm():

    api_key = st.secrets.get(
        "GROQ_API_KEY",
        os.getenv("GROQ_API_KEY")
    )

    if not api_key:
        raise ValueError(
            "Missing GROQ_API_KEY in Streamlit Secrets"
        )

    return ChatGroq(
        groq_api_key=api_key,
        model_name="llama3-8b-8192"
    )
