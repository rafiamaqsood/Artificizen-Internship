from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse

from app.services.cache import get, set
from app.services.embeddings import embed_text
from app.services.qdrant_service import search
from app.services.session import get_history, add_message
from app.services.groq_service import ask_groq
from app.services.groq_service import ask_groq_stream
from app.utils.prompt import build_prompt

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    cached_response = get(request.session_id,request.query)
    if cached_response:
        return cached_response


    history = get_history(request.session_id)

    retrieval_query = request.query

    if history:
        last_user_messages = [
            msg["content"]
            for msg in history
            if msg["role"] == "user"
        ]

        if last_user_messages:
            retrieval_query = (
                last_user_messages[-1]
                + " "
                + request.query
            )

    query_embedding = embed_text(retrieval_query)

    results = search(query_embedding)

    context = "\n\n".join(
        point.payload["text"]
        for point in results
    )
    sources = [
        {
            "filename": point.payload["filename"],
            "chunk_index": point.payload["chunk_index"]
        }
        for point in results
    ]

    history = get_history(request.session_id)

    history_text = "\n".join(
        f"{msg['role']}: {msg['content']}"
        for msg in history
    )
    print("History")
    print(history_text)

    prompt = build_prompt(
        context=context,
        history=history_text,
        query=request.query
    )
    print(prompt)

    answer = ask_groq(prompt)

    add_message(request.session_id, "user", request.query)
    add_message(request.session_id, "assistant", answer)

    response = ChatResponse(
        answer=answer,
        sources=sources
    )
    set( request.session_id,request.query, response)
    return response


@router.post("/stream")
def chat_stream(request: ChatRequest):

    query_embedding = embed_text(request.query)

    results = search(query_embedding)
    context = "\n\n".join(
        point.payload["text"]
        for point in results
    )
    history = get_history(request.session_id)

    history_text = "\n".join(
        f"{msg['role']}: {msg['content']}"
        for msg in history
    )
    print("History")
    print(history_text)
    prompt = build_prompt(
        context=context,
        history=history_text,
        query=request.query
    )
    print(prompt)

    def generate():
        answer = ""

        for token in ask_groq_stream(prompt):
            answer += token
            yield token

        add_message(request.session_id, "user", request.query)
        add_message(request.session_id, "assistant", answer)

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )