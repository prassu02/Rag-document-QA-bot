import os
import fitz  # PyMuPDF
from docx import Document


# -------------------------
# PDF Loader (with page metadata)
# -------------------------
def load_pdf(file_path):
    doc = fitz.open(file_path)

    pages = []
    for page_num, page in enumerate(doc):
        text = page.get_text()
        if text.strip():
            pages.append((page_num + 1, text))  # page metadata

    return pages


# -------------------------
# TXT Loader
# -------------------------
def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [(None, f.read())]


# -------------------------
# DOCX Loader
# -------------------------
def load_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return [(None, text)]


# -------------------------
# Main Loader
# -------------------------
def load_documents(folder="data"):
    docs = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if file.endswith(".pdf"):
            content = load_pdf(path)
            for page_num, text in content:
                docs.append({
                    "filename": file,
                    "page": page_num,
                    "text": text
                })

        elif file.endswith(".txt"):
            content = load_txt(path)
            docs.append({
                "filename": file,
                "page": None,
                "text": content[0][1]
            })

        elif file.endswith(".docx"):
            content = load_docx(path)
            docs.append({
                "filename": file,
                "page": None,
                "text": content[0][1]
            })

    return docs