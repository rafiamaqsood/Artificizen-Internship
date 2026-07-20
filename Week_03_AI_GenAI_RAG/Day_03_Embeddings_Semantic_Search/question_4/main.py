# Repeat the previous exercise using Qdrant (QdrantClient(':memory:')). Add payloads with a source field and filter results to only return documents where source == 'manual'.

from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue,
)
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(":memory:")

client.create_collection(
    collection_name="paragraphs",
    vectors_config=VectorParams(
        size=384,              
        distance=Distance.COSINE
    )
)

paragraphs = [
    "Python is a popular programming language used for AI and web development.",
    "Machine learning allows computers to learn from data.",
    "Artificial intelligence is transforming many industries.",
    "Dogs enjoy playing with their owners.",
    "Cats spend much of their day sleeping.",
    "Birds build nests to protect their eggs.",
    "The Earth revolves around the Sun.",
    "The Pacific Ocean is the largest ocean on Earth.",
    "Football is one of the world's most popular sports.",
    "Databases are used to efficiently store and retrieve information."
]

embeddings = model.encode(paragraphs)

points = []

for i, (paragraph, embedding) in enumerate(zip(paragraphs, embeddings)):
    points.append(
        PointStruct(
            id=i,
            vector=embedding.tolist(),
            payload={
                "text": paragraph,
                "source": "manual" if i < 5 else "website"
            }
        )
    )

client.upsert(
    collection_name="paragraphs",
    points=points
)

query = "Which programming language is best for artificial intelligence?"

query_embedding = model.encode(query)

results = client.query_points(
    collection_name="paragraphs",
    query=query_embedding.tolist(),
    query_filter=Filter(
        must=[
            FieldCondition(
                key="source",
                match=MatchValue(value="manual")
            )
        ]
    ),
    limit=2
).points

print("Top 2 Results:\n")

for i, result in enumerate(results, start=1):
    print(f"Rank {i}")
    print(f"Score  : {result.score:.4f}")
    print(f"Source : {result.payload['source']}")
    print(f"Text   : {result.payload['text']}")
    print()