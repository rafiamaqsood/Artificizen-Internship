from Day_03_Embeddings_Semantic_Search.question_6.utility_function import client, model
def retrieve(query, collection="chunks", top_k=3):

    query_embedding = model.encode(query)

    results = client.query_points(
        collection_name=collection,
        query=query_embedding.tolist(),
        limit=top_k
    )

    return [point.payload["text"] for point in results.points]