import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

DATA_DIR="data"


def load_documents():

    docs=[]

    if not os.path.exists(DATA_DIR):
        raise FileNotFoundError(
            "data folder not found"
        )

    pdf_files=[
        f for f in os.listdir(DATA_DIR)
        if f.endswith(".pdf")
    ]

    if len(pdf_files)==0:
        raise ValueError(
            "No PDF files in data folder"
        )

    for file in pdf_files:
        path=os.path.join(DATA_DIR,file)
        loader=PyMuPDFLoader(path)
        docs.extend(loader.load())

    splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks=splitter.split_documents(docs)

    return chunks
