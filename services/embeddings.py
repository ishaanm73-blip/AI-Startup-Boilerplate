from sentence_transformers import SentenceTransformer
import chromadb
model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client()
collection = client.create_collection("documents")
def search(query,top_k=3):
    q_embedding = model.encode([query]).tolist()[0]
    results = collection.query(
        query_embedding = [q_embedding],
        n_results = top_k
    )
    documents = results["documents"][0]
    return documents
