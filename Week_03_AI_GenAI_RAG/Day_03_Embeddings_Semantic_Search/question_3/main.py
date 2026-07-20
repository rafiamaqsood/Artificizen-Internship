# Create a ChromaDB in-memory collection, add 10 short paragraphs from any topic, query it with a natural language question, and print the top-2 results.

import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()

collection = client.create_collection(name="paragraphs")

paragraphs = [
    "Python is a popular programming language used for web development, AI, and automation.",
    "Machine learning enables computers to learn patterns from data without explicit programming.",
    "Artificial intelligence is transforming healthcare, education, and finance.",
    "Dogs are loyal pets that enjoy playing with their owners and fetching balls.",
    "Cats are independent animals that spend much of their time sleeping and grooming.",
    "Birds build nests to protect their eggs and raise their young safely.",
    "The Earth revolves around the Sun once every 365 days.",
    "The Pacific Ocean is the largest and deepest ocean on Earth.",
    "Football is one of the most popular sports played around the world.",
    "Databases store, organize, and retrieve information efficiently for applications."
]

ids = [str(i) for i in range(1, len(paragraphs) + 1)]

embeddings = model.encode(paragraphs)
collection.add(
    ids=ids,
    documents=paragraphs,
    embeddings=embeddings.tolist()
)
query = "Which programming language is commonly used for artificial intelligence?"
query_embedding = model.encode(query)

results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=2
)

print("Top 2 Most Similar Paragraphs:\n")

documents = results["documents"][0]
distances = results["distances"][0]

for i in range(len(documents)):
    similarity = 1 - distances[i] 
    print(f"Rank {i + 1}")
    print(f"Paragraph: {documents[i]}")
    print(f"Similarity Score: {similarity:.4f}\n")