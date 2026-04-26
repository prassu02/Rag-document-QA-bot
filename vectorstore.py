import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")

class VectorStore:
    def __init__(self, dim=384):
        self.index = faiss.IndexFlatL2(dim)
        self.chunks = []

    def add(self, embeddings, chunks):
        self.index.add(np.array(embeddings).astype("float32"))
        self.chunks.extend(chunks)

    def search(self, query_embedding, k=3):
        D, I = self.index.search(np.array([query_embedding]), k)
        return [self.chunks[i] for i in I[0]]

    def save(self, path="store.pkl"):
        with open(path, "wb") as f:
            pickle.dump((self.index, self.chunks), f)

    def load(self, path="store.pkl"):
        with open(path, "rb") as f:
            self.index, self.chunks = pickle.load(f)