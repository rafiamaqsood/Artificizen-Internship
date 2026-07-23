# Implement a simple cache: hash the query string with hashlib.md5, store results in a dict, and return cached answers immediately on repeated queries. Log whether each request was a cache hit or miss.

from fastapi import FastAPI 
from pydantic import BaseModel
from pathlib import Path
import sys
import hashlib
import logging

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
    session_id: str
    query: str

pdf = PROJECT_ROOT / "Day_04_RAG" / "Week3_AI_GenAI_RAG.pdf"
prepare_document(pdf)

conversation_history = {}
cache = {}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

@app.post("/chat")
def chat(request: ChatRequest):
    history = conversation_history.get(
        request.session_id,
        []
    )
    query_hash = hashlib.md5(
        request.query.encode()
    ).hexdigest()
    if query_hash in cache:
        logger.info("Cache Hit")
        return cache[query_hash]
    logger.info("Cache Miss")

    retrieved = retrieve(request.query)
    retrieved = [
        point
        for point in retrieved
        if point.score > 0.4
    ]
    if not retrieved:
        return {
            "answer": "I don't know.",
            "sources": []
        }

    texts = []

    for point in retrieved:
        texts.append(point.payload["text"])

    prompt = build_prompt(request.query, texts)

    answer = ask(
        prompt=prompt,
        history=history,
    )
    history.append({
        "role": "user",
        "content": request.query
    })

    history.append({
        "role": "assistant",
        "content": answer
    })
    history = history[-6:]
    conversation_history[request.session_id] = history
    logger.info("Conversation History: %s", conversation_history)

    sources = []

    for point in retrieved:
        sources.append({
            "source": point.payload["source"],
            "chunk_index": point.payload["chunk_index"],
            "score": round(point.score, 4)
        })
    response = {
        "answer": answer,
        "sources": sources
    }
    cache[query_hash] = response
    return response

