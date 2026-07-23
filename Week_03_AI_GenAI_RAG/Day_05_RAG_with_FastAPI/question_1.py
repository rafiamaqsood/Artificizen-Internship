# Expose your Day 4 RAG pipeline as POST /chat in FastAPI. The response body must include answer (string) and sources (list of chunk metadata dicts).

from fastapi import FastAPI
from pydantic import BaseModel

from pathlib import Path
import sys
BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

sys.path.append(str(PROJECT_ROOT))
sys.path.append(str(PROJECT_ROOT / "Day_04_RAG"))

from utils.document_loader import prepare_document
from utils.retrieval import retrieve
from utils.build_prompt import build_prompt
from wrapper_function import ask

app = FastAPI()

class ChatRequest(BaseModel):
    query: str

pdf = PROJECT_ROOT / "Day_04_RAG" / "Week3_AI_GenAI_RAG.pdf"
prepare_document(pdf)

@app.post("/chat")
def chat(request: ChatRequest):

    retrieved = retrieve(request.query)

    texts = []

    for point in retrieved:
        texts.append(point.payload["text"])

    prompt = build_prompt(request.query, texts)

    answer = ask(
        prompt=prompt,
    )

    sources = []

    for point in retrieved:
        sources.append({
            "source": point.payload["source"],
            "chunk_index": point.payload["chunk_index"],
            "score": round(point.score, 4)
        })

    return {
        "answer": answer,
        "sources": sources
    }