# Add streaming using FastAPI’s StreamingResponse and stream=True on the Groq call. Verify tokens appear progressively with a curl command or the browser.

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from pathlib import Path
import hashlib
import sys
import time

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


def generate_response(prompt, history):
    stream = ask(
        prompt=prompt,
        history=history,
        stream=True
    )

    answer = ""

    for chunk in stream:
        if chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            answer += token
            yield token
            time.sleep(0.1)

    return answer


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
        print("Cache Hit")
        cached = cache[query_hash]

        return StreamingResponse(
            iter([cached["answer"]]),
            media_type="text/plain"
        )

    print("Cache Miss")

    retrieved = retrieve(
        request.query,
        collection="chunks",
        top_k=3
    )

    retrieved = [
        point
        for point in retrieved
        if point.score > 0.40
    ]

    if not retrieved:
        answer = "I don't know."
        cache[query_hash] = {
            "answer": answer
        }

        return StreamingResponse(
            iter([answer]),
            media_type="text/plain"
        )

    texts = []

    for point in retrieved:
        texts.append(point.payload["text"])

    prompt = build_prompt(
        request.query,
        texts
    )

    history.append({
        "role": "user",
        "content": request.query
    })
    conversation_history[request.session_id] = history[-6:]

    def stream():
        answer = ""
        response = ask(
            prompt=prompt,
            history=history,
            stream=True
        )
        for chunk in response:
            if chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                answer += token
                yield token

        history.append({
            "role": "assistant",
            "content": answer
        })
        conversation_history[request.session_id] = history[-6:]
        cache[query_hash] = {
            "answer": answer,
            "sources": [
                {
                    "source": point.payload["source"],
                    "chunk_index": point.payload["chunk_index"],
                    "score": round(point.score, 4)
                }
                for point in retrieved
            ]
        }
        print("\nConversation History")
        print(conversation_history)
    return StreamingResponse(
        stream(),
        media_type="text/plain"
    )