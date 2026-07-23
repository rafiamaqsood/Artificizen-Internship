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

pdf = PROJECT_ROOT / "Day_04_RAG" / "Week3_AI_GenAI_RAG.pdf"
prepare_document(pdf)


def rag(query):
    retrieved = retrieve(query)

    chunks = [
        point.payload["text"]
        for point in retrieved
    ]

    prompt = build_prompt(query, chunks)

    return ask(
        prompt=prompt,
        model="llama-3.3-70b-versatile",
        temperature=0
    )


test_cases = [
    {
        "question": "What is RAG?",
        "expected": "Retrieval-Augmented Generation solves the knowledge cutoff problem."
    },
    {
        "question": "Why is chunk overlap important?",
        "expected": "It preserves context across chunk boundaries."
    },
    {
        "question": "What library is used to read PDF files?",
        "expected": "pymupdf4llm"
    },
    {
        "question": "Which model is recommended for generation?",
        "expected": "llama-3.3-70b-versatile"
    },
    {
        "question": "Who invented Python?",
        "expected": "I don't know."
    }
]

correct = 0

for i, test in enumerate(test_cases, start=1):

    answer = rag(test["question"])
    expected = test["expected"].lower()
    answer_lower = answer.lower()

    if expected == "i don't know.":
        if "i don't know" in answer_lower:
            result = "Correct"
            correct += 1
        else:
            result = "Wrong"

    elif all(keyword in answer_lower for keyword in expected.split()):
        result = "Correct"
        correct += 1

    elif any(keyword in answer_lower for keyword in expected.split()):
        result = "Partially Correct"
        correct += 0.5

    else:
        result = "Wrong"

    print("=" * 80)
    print(f"Question : {test['question']}")
    print(f"Expected : {test['expected']}")
    print(f"Answer   : {answer}")
    print(f"Result   : {result}")
    print()

accuracy = (correct / len(test_cases)) * 100

print("=" * 80)
print(f"Accuracy: {accuracy:.2f}%")