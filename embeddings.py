from langchain.embeddings import OpenAIEmbeddings

# Embedding-Modell
embedding = OpenAIEmbeddings()

texts = ["Wie funktioniert eine Wärmepumpe?",
         "Was ist das Prinzip einer Wärmepumpe?"]

# Vektor
vectors = embedding.embed_documents(texts)

print(vectors[0][:5])
