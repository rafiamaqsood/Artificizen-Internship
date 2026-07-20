# Write a function semantic_search(query, documents) that embeds the query, embeds all documents, and returns the top-3 most similar documents with their cosine similarity scores.

from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_search(query, documents):
    query_embedding = model.encode(query)
    doc_embeddings = model.encode(documents)

    results = []

    # Compute query norm once
    query_norm = np.linalg.norm(query_embedding)

    for i in range(len(documents)):
        dot_product = np.dot(query_embedding, doc_embeddings[i])

        doc_norm = np.linalg.norm(doc_embeddings[i])

        similarity = dot_product / (query_norm * doc_norm)

        results.append((documents[i], similarity))

    results.sort(key=lambda x: x[1], reverse=True)

    return results[:3]

documents = [
    "A dog is chasing a ball.",
    "Cats love sleeping on sofas.",
    "Dogs enjoy playing fetch.",
    "Artificial Intelligence is transforming industries.",
    "A puppy is running after a toy."
]

query = "A dog is playing with a ball."

top_results = semantic_search(query, documents)

print("Top 3 Most Similar Documents:\n")

for rank, (doc, score) in enumerate(top_results, start=1):
    print(f"{rank}. {doc}")
    print(f"   Similarity Score: {score:.4f}\n")