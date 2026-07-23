# Add conversation history: store the last 6 turns in memory per session and pass them as previous messages to Groq so follow-up questions work correctly.

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
    session_id: str
    query: str

pdf = PROJECT_ROOT / "Day_04_RAG" / "Week3_AI_GenAI_RAG.pdf"
prepare_document(pdf)

conversation_history = {}

@app.post("/chat")
def chat(request: ChatRequest):
    history = conversation_history.get(
        request.session_id,
        []
    )
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
    print("\nConversation History:")
    print(conversation_history)

    sources = []

    for point in retrieved:
        sources.append({
            "source": point.payload["source"],
            "chunk_index": point.payload["chunk_index"],
            "score": round(point.score, 4)
        })
    return{
        "answer": answer,
        "sources": sources
    }

