# •	Ingestion endpoint POST /ingest: accepts a plain-text or PDF file upload, chunks it, embeds all chunks with sentence-transformers, and stores them in Qdrant with source filename and chunk index as metadata

from fastapi import APIRouter, UploadFile, File, HTTPException
import os

from app.utils.pdf_loader import read_pdf
from app.services.chunking import chunk_text
from app.services.embeddings import embed_text
from app.services.qdrant_service import insert_chunks

router = APIRouter(prefix="/ingest", tags=["Ingest"])

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/")
async def ingest_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = read_pdf(file_path)
    chunks = chunk_text(text)
    embeddings = embed_text(chunks)
    insert_chunks(chunks, embeddings, file.filename)
    return {
        "message": "PDF ingested successfully.",
        "chunk_count": len(chunks)
    }