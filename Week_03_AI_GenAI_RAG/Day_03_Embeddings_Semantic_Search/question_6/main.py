# Write a utility embed_and_store(texts, metadata_list, collection) that batch-embeds a list of strings and upserts them into a Qdrant collection with metadata. You will reuse this directly in the RAG pipeline tomorrow.

from utility_function import embed_and_store

texts = [
    "Python is widely used in Artificial Intelligence.",
    "Dogs are loyal animals.",
    "Machine learning analyzes data."
]

metadata = [
    {"source": "manual", "doc_id": 1},
    {"source": "website", "doc_id": 2},
    {"source": "manual", "doc_id": 3}
]

embed_and_store(
    texts,
    metadata,
    "documents"
)