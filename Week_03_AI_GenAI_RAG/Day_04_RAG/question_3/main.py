# Write a retrieve(query, collection, top_k=3) function that embeds the query with sentence-transformers and returns the top-k chunks from Qdrant.

from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
from utils.document_loader import prepare_document
from utils.retrieval import retrieve

pdf = BASE_DIR / "Week3_AI_GenAI_RAG.pdf"
prepare_document(pdf)

results = retrieve(
    query="What is zero-shot prompting?",
    collection="chunks",
    top_k=3
)

for i, chunk in enumerate(results, start=1):
    print(f"Result {i}:")
    print(f"{chunk}\n")
