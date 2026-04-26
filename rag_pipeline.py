import os
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer

# Load env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=api_key)

# Embedding model (RAG retrieval)
embedder = SentenceTransformer("all-MiniLM-L6-v2")


# -----------------------------
# Embedding function
# -----------------------------
def get_embedding(text):
    return embedder.encode(text)


# -----------------------------
# LLM Answer Generator (FIXED)
# -----------------------------
def generate_answer(question, context_chunks):

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a strict RAG-based AI assistant.

RULES:
- Use ONLY the provided context
- Do NOT use outside knowledge
- If answer is not present, say "Not found in documents"

CONTEXT:
{context}

QUESTION:
{question}

FORMAT:
- Clear answer
- Mention source filename if available
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content