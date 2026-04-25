import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 4

DATA_PATH="data/"
DB_PATH="vector_store/faiss_index"