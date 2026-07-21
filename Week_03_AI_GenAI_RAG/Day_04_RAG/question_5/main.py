# Wire everything together: retrieve() → build_prompt() → ask() (using Groq). Ask three questions — two with answers in the document and one without. Verify the model says “I don’t know” for the third.

from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = BASE_DIR.parent

sys.path.append(str(BASE_DIR))
sys.path.append(str(PROJECT_ROOT))

from utils.document_loader import prepare_document
from utils.retrieval import retrieve
from utils.build_prompt import build_prompt
from wrapper_function import ask


pdf = BASE_DIR / "Week3_AI_GenAI_RAG.pdf"
prepare_document(pdf)

def rag(query):
    chunks = retrieve(query)
    prompt = build_prompt(query, chunks)
    return ask(
        prompt=prompt,
        model="llama-3.3-70b-versatile",
        temperature=0
    )

questions = [
    "What is zero-shot prompting?",
    "What is RAG?",
    "Who invented Python?"
]

for question in questions:
    print(f"{question}\n")
    print(f"{rag(question)}\n")
