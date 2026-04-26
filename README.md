# 📄 RAG Document Q&A Bot (Groq + FAISS)

An end-to-end Retrieval-Augmented Generation (RAG) system that allows users to ask questions over a custom set of documents and receive accurate, context-grounded answers with source citations.

The system uses FAISS for vector search, SentenceTransformers for embeddings, and Groq LLM for fast response generation. It also includes reranking and keyword filtering to improve retrieval accuracy.

---

## 🚀 Features

- 📄 Supports PDF, TXT, and DOCX documents
- 🔍 Semantic search using FAISS vector database
- 🧠 Embedding-based retrieval using SentenceTransformers
- ⚡ Fast LLM inference using Groq API (LLaMA models)
- 🎯 Cross-encoder reranking for better relevance
- 🔎 Keyword-based filtering for improved precision
- 💬 Streamlit-based interactive UI
- 📌 Source-based grounded answers (no hallucination)

---

## 🧠 Architecture Overview

User Query
   ↓
Sentence Embedding Model
   ↓
FAISS Vector Search (Top-K retrieval)
   ↓
Keyword Filtering Layer
   ↓
Cross-Encoder Reranking
   ↓
Context Preparation
   ↓
Groq LLM (Answer Generation)
   ↓
Final Answer + Source Chunks

---

## 🧰 Tech Stack

- Python 3.11+
- Streamlit
- FAISS (Facebook AI Similarity Search)
- SentenceTransformers
- Cross-Encoder (ms-marco-MiniLM-L-6-v2)
- Groq API (LLaMA 3)
- PyMuPDF (PDF parsing)
- python-docx (DOCX parsing)

---

## 📂 Project Structure

```

rag-document-qa-bot/
│
├── app.py
├── ingest.py
├── utils.py
├── vectorstore.py
├── rag_pipeline.py
├── reranker.py
├── retrieval_utils.py
│
├── data/
│   ├── Machine_Learning.pdf
│   ├── Deep_Learning.pdf
│   ├── ...
│
├── .env
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/your-username/rag-document-qa-bot.git
cd rag-document-qa-bot
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add environment variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

### 4. Run the application

```bash
streamlit run app.py
```

---

## 📌 Example Queries

* What is machine learning?
* Explain reinforcement learning
* What is deep learning?
* How does backpropagation work?
* What is AutoML?

---

## ⚠️ Known Limitations

* Does not support scanned PDFs (no OCR)
* Performance depends on embedding quality
* Limited context window for large documents
* No long-term memory across sessions

---

## 📊 Future Improvements

* Add hybrid search (BM25 + FAISS)
* Add chat memory (multi-turn conversations)
* Add PDF page-level citation highlighting
* Deploy on Streamlit Cloud / HuggingFace Spaces
* Add evaluation metrics dashboard

---

## 🎯 Key Learning Outcome

This project demonstrates:

* RAG pipeline design
* Vector database usage
* LLM integration (Groq API)
* Retrieval optimization (filtering + reranking)
* Real-world AI system architecture

---

## 👨‍💻 Author

Prasanna Kumar
AI & Data Science Enthusiast
