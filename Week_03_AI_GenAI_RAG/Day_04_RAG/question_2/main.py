# Load a plain-text or PDF file, chunk it, embed all chunks with sentence-transformers, and store them in Qdrant with source filename and chunk index as metadata.
from pathlib import Path
import sys
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
from utils.document_loader import prepare_document

pdf = Path(__file__).resolve().parents[1] / "Week3_AI_GenAI_RAG.pdf"
prepare_document(pdf)
