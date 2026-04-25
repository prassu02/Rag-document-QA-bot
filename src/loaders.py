from langchain_community.document_loaders import PyMuPDFLoader
import os

def load_documents():
    docs=[]

    for file in os.listdir("data"):
        if file.endswith(".pdf"):
            loader = PyMuPDFLoader(
                os.path.join("data", file)
            )
            docs.extend(loader.load())

    return docs
