# RAG pipeline integrating retriever and generator
from .retriever import retrieve_documents
from .generator import generate_answer

def rag_pipeline(query):
    docs = retrieve_documents(query)
    return generate_answer(docs, query)
