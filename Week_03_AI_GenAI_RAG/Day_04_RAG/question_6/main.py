# Test hallucination: run the same question WITHOUT the RAG context (raw Groq call only).Compare the answer to the RAG answer. Write a short observation.

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
    chunks = retrieve(
        query=query,
        collection="chunks",
        top_k=3
    )
    prompt = build_prompt(query, chunks)
    return ask(
        prompt=prompt,
        model="llama-3.3-70b-versatile",
        temperature=0
    )
question = "Who invented Python?"

# Without RAG
raw_answer = ask(
    prompt=question,
    model="llama-3.3-70b-versatile",
    temperature=0
)

# With RAG
rag_answer = rag(question)

print(f"Question: {question}")
print(f"\nRaw Groq Answer: {raw_answer}")
print(f"\nRAG Answer: {rag_answer}")
print("\nObservation:")
print(
    "The raw Groq model answered using its pre-trained knowledge. "
    "The RAG system answered only from the retrieved document context. "
    "Since the document did not contain information about who invented Python, "
    "the RAG system correctly responded with 'I don't know'. "
    "This makes the RAG answer more grounded and reduces hallucinations."
)