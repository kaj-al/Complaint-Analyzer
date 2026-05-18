import pandas as pd
from langchain_core.documents import Document
import re
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import BM25Retriever

def clean(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9]', '', text)
    return text.strip()

df = pd.read_csv("Datasetprojpowerbi.csv")
documents = []
for index, row in df.iterrows():
    text = clean(row["Reports"])
    doc = Document(page_content=text, metadata={"Category": row["Category"]})
    documents.append(doc)

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# vectorstore
vectorstore = FAISS.from_documents(documents, embedding_model)
vectorstore.save_local("store/")

# reteriever
retriever = BM25Retriever.from_documents(documents)
retriever.k = 5

dense_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# hybrid retriever
def hybrid(query):
    dense = dense_retriever.invoke(query)
    sparse = retriever.invoke(query)
    combine = dense + sparse
    unique = []
    seen = set()
    for doc in combine:
        if doc.page_content not in seen:
            unique.append(doc)
            seen.add(doc.page_content)
    return unique[:5]     

