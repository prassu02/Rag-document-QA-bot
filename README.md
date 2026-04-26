# 📄 RAG Document Q&A Bot (Groq + FAISS)

A Retrieval-Augmented Generation (RAG) system that allows users to upload documents and ask natural language questions. The system retrieves relevant context using FAISS vector search and generates accurate, grounded answers using Groq LLM.

---

## 🚀 Features

- 📄 Supports PDF, TXT, and DOCX documents  
- 🔍 Semantic search using FAISS vector database  
- 🧠 SentenceTransformer embeddings for similarity search  
- ⚡ Fast LLM inference using Groq API (LLaMA models)  
- 🎯 Cross-encoder reranking for better retrieval accuracy  
- 🔎 Keyword filtering for precision improvement  
- 💬 Streamlit interactive UI  
- 📌 Source-based grounded answers (reduces hallucination)

---

## 🧠 Architecture

User Query  
↓  
Embedding (SentenceTransformer)  
↓  
FAISS Vector Search (Top-K retrieval)  
↓  
Keyword Filtering  
↓  
Cross-Encoder Reranking  
↓  
Context Selection  
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
├── app.py                  # Streamlit UI
├── ingest.py               # Document loader
├── utils.py                # Chunking logic
├── vectorstore.py         # FAISS implementation
├── rag_pipeline.py        # LLM + embeddings
├── reranker.py            # Cross-encoder reranking
├── retrieval_utils.py     # Keyword filtering
│
├── data/                  # Input documents
│   ├── Machine_Learning.pdf
│   ├── Deep_Learning.pdf
│   ├── Generative_AI.pdf
│   ├── NLP.pdf 
│   ├── AI_Fundamentals.pdf
|
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

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Add environment variables

Create a `.env` file:

```bash
GROQ_API_KEY=your_api_key_here
```

---

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📌 Example Queries

* What is machine learning?
* Explain reinforcement learning
* What is deep learning?
* How does backpropagation work?
* What is Generative AI?

---

## ⚠️ Known Limitations

* Does not support scanned PDFs (no OCR)
* Performance depends on embedding quality
* Limited context window for large documents
* No persistent chat memory

---

## 📈 Future Improvements

* Hybrid search (BM25 + FAISS)
* Chat memory for multi-turn conversations
* PDF page-level highlighting for citations
* Deployment on Streamlit Cloud
* Evaluation dashboard for retrieval quality

---

## 🎯 Key Learnings

This project demonstrates:

* Retrieval-Augmented Generation (RAG) pipeline design
* Vector database usage (FAISS)
* LLM integration (Groq API)
* Embedding-based semantic search
* Retrieval optimization techniques
* End-to-end AI system architecture

---

## 👨‍💻 Author

**Prasanna Kumar**
AI & Data Science Enthusiast

