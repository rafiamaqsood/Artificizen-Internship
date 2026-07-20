# Use sentence-transformers with all-MiniLM-L6-v2 to embed “A dog is chasing a ball” and five other sentences. Compute cosine similarity between all pairs using numpy and rank them from most to least similar.

import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    "A dog is chasing a ball",
    "Dog is playing with a ball",
    "A dog is chasing a cat",
    "Cat is chasing a mouse",
    "Dog is playing with a cat",
    "A sparrow is feeding its baby"
]

embeddings = model.encode(texts)

pairs = []

for i in range(len(texts)):
    for j in range(i + 1, len(texts)):

        dot_product = np.dot(embeddings[i], embeddings[j])

        norm_a = np.linalg.norm(embeddings[i])
        norm_b = np.linalg.norm(embeddings[j])

        similarity = dot_product / (norm_a * norm_b)

        pairs.append((texts[i], texts[j], similarity))

pairs.sort(key=lambda x: x[2], reverse=True)

for s1, s2, score in pairs:
    print(f"{score:.4f}")
    print(f"{s1}")
    print(f"{s2}\n")