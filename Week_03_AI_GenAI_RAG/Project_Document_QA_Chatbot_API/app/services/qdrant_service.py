from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct
)
from app.config import COLLECTION_NAME

client = QdrantClient(":memory:")

collections = client.get_collections().collections
collection_names = [collection.name for collection in collections]

if COLLECTION_NAME not in collection_names:
    client.create_collection(
        collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
    )

def insert_chunks(chunks, embeddings, filename):
    points = []
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        points.append(
            PointStruct(
                id=i,
                vector=embedding,
                payload={
                    "text": chunk,
                    "filename": filename,
                    "chunk_index": i
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )


def search(embedding):
    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=embedding,
        limit=5
    )
    return results.points