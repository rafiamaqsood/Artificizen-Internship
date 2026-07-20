# Embed 50 random sentences, then query with a sentence that is semantically close but uses completely different words. Verify that semantic search still finds the right match.

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "A dog is chasing a ball in the park.",
    "A cat is sleeping on the sofa.",
    "Python is a popular programming language.",
    "Machine learning helps computers learn from data.",
    "Artificial intelligence is changing healthcare.",
    "The Earth revolves around the Sun.",
    "The Moon orbits the Earth.",
    "Football is played by two teams.",
    "Basketball is played with a hoop.",
    "Birds build nests in trees.",
    "Fish swim in rivers and oceans.",
    "Cars need fuel or electricity to move.",
    "Electric vehicles are becoming more popular.",
    "Rain falls from clouds.",
    "Snow covers mountains during winter.",
    "Books are a great source of knowledge.",
    "Reading improves vocabulary.",
    "Students attend school to gain education.",
    "Teachers help students understand concepts.",
    "Databases store large amounts of information.",
    "SQL is used to manage relational databases.",
    "Cloud computing provides online resources.",
    "Cybersecurity protects computer systems.",
    "Hackers attempt to exploit vulnerabilities.",
    "The internet connects billions of devices.",
    "Dogs are loyal companions.",
    "Cats enjoy chasing mice.",
    "A chef prepares delicious meals.",
    "Baking requires flour, sugar, and eggs.",
    "Coffee contains caffeine.",
    "Tea is enjoyed around the world.",
    "Exercise improves physical health.",
    "Walking every day is beneficial.",
    "Swimming is an excellent full-body workout.",
    "Mountains attract hikers.",
    "Traveling helps people experience new cultures.",
    "Photography captures memorable moments.",
    "Music can improve mood.",
    "The guitar is a popular musical instrument.",
    "Pianos have eighty-eight keys.",
    "Space exploration advances science.",
    "Astronauts travel beyond Earth.",
    "Trees produce oxygen.",
    "Plants require sunlight to grow.",
    "Recycling helps protect the environment.",
    "Solar panels generate renewable energy.",
    "Wind turbines produce electricity.",
    "A puppy is running after a toy in the garden.",
    "Children enjoy playing outside.",
    "Libraries contain thousands of books."
]

doc_embeddings = model.encode(documents)

query = "A young dog is happily running after its plaything outdoors."

query_embedding = model.encode(query)

similarities = cosine_similarity(
    [query_embedding],
    doc_embeddings
)[0]

results = []

for i in range(len(documents)):
    results.append((documents[i], similarities[i]))

results.sort(key=lambda x: x[1], reverse=True)

print(f"Query: {query}\n")

print("Top 5 Most Similar Sentences:\n")

for rank, (sentence, score) in enumerate(results[:5], start=1):
    print(f"{rank}. {sentence}")
    print(f"   Similarity Score: {score:.4f}\n")