# Write a chunk_text(text, chunk_size=500, overlap=50) function that splits a long string into overlapping chunks. Print the number of chunks produced from a 3,000-word document.

from pathlib import Path
import sys
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
import pymupdf4llm
from utils.chunking import chunk_text

pdf = Path(__file__).resolve().parents[1] / "Week3_AI_GenAI_RAG.pdf"
text = pymupdf4llm.to_markdown(str(pdf))
chunks = chunk_text(text)
print("Number of chunks:", len(chunks))
print (chunks[0])
