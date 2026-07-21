from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct
)
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(":memory:")
def embed_and_store(texts, metadata_list, collection_name):
    if not client.collection_exists(collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

    embeddings = model.encode(texts)

    points = []

    for i, (text, embedding, metadata) in enumerate(
        zip(texts, embeddings, metadata_list)
    ):
        payload = metadata.copy()
        payload["text"] = text

        points.append(
            PointStruct(
                id=i,
                vector=embedding.tolist(),
                payload=payload
            )
        )

    client.upsert(
        collection_name=collection_name,
        points=points
    )

    print(f"{len(points)} documents stored successfully!")