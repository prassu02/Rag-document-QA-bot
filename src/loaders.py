import os
import fitz
from langchain_core.documents import Document

def load_documents(data_path):

    docs=[]

    for file in os.listdir(data_path):

        if file.endswith(".pdf"):

            pdf_path=os.path.join(data_path,file)

            pdf=fitz.open(pdf_path)

            for page_num,page in enumerate(pdf):

                text=page.get_text()

                docs.append(
                    Document(
                        page_content=text,
                        metadata={
                            "source":file,
                            "page":page_num+1
                        }
                    )
                )
    return docs