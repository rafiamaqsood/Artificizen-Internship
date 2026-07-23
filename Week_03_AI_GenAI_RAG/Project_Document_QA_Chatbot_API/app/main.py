from fastapi import FastAPI

from app.api.ingestion_pipeline import router as ingest_router
from app.api.chat import router as chat_router

app = FastAPI(
    title="RAG Chatbot API")

app.include_router(ingest_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "RAG Chatbot API is running"}