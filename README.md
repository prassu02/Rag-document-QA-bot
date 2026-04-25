# RAG Document Q&A Bot

A Retrieval-Augmented Generation (RAG) application that answers questions from PDF documents using semantic search and large language models.

## Features

- PDF document ingestion
- Text chunking
- Embeddings using HuggingFace
- FAISS vector database
- Semantic retrieval
- LLM-powered question answering using Groq + Llama
- Streamlit web interface
- CLI chatbot version
- Source citations with retrieved chunks

---

## Architecture

```text
PDF Documents
   ↓
Document Loading
   ↓
Text Chunking
   ↓
Embeddings (all-MiniLM-L6-v2)
   ↓
FAISS Vector Store
   ↓
Top-K Retrieval
   ↓
Groq LLM (Llama 3.3 70B)
   ↓
Answer + Sources + Retrieved Chunks
```

---

## Tech Stack

- Python
- LangChain
- HuggingFace Embeddings
- FAISS
- Groq API
- Streamlit

---

## Project Structure

```text
rag-document-qa-bot/
│
├── data/
│   ├── AI_Fundamentals.pdf
│   ├── Machine_Learning.pdf
│   └── ...
│
├── src/
│   ├── loaders.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── rag_chain.py
│   └── index_documents.py
│
├── vector_store/
├── app.py
├── cli_bot.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd rag-document-qa-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create environment variable:

```bash
GROQ_API_KEY=your_api_key
```

Windows PowerShell:

```powershell
$env:GROQ_API_KEY="your_api_key"
```

---

## Build Vector Index

```bash
python -m src.index_documents
```

---

## Run CLI Bot

```bash
python cli_bot.py
```

Example:

```text
Ask: What is Machine Learning?
```

---

## Run Streamlit App

```bash
streamlit run app.py
```

---

## Sample Questions

Try asking:

- What is Artificial Intelligence?
- What is Machine Learning?
- Explain supervised vs unsupervised learning
- What is reinforcement learning?
- What is Generative AI?

---

## Example Output

- Answer generated from documents
- Source citations:

```text
Machine_Learning.pdf | Page 1
```

- Retrieved chunks shown for transparency

---

## Future Improvements

- Conversational memory
- Hybrid search (BM25 + FAISS)
- Reranking
- User PDF upload
- Multi-document chat
- Advanced RAG pipelines

---

## Author

Prasanna Kumar  
Machine Learning Engineer | AI | Data Science