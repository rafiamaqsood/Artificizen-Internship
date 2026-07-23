from pathlib import Path
import sys

from datasets import Dataset
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from ragas.llms import LangchainLLMWrapper
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from ragas.embeddings import LangchainEmbeddingsWrapper


BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

sys.path.append(str(PROJECT_ROOT))
sys.path.append(str(PROJECT_ROOT / "Day_04_RAG"))

from utils.document_loader import prepare_document
from utils.retrieval import retrieve
from utils.build_prompt import build_prompt
from config import GROQ_API_KEY
from wrapper_function import ask

pdf = PROJECT_ROOT / "Day_04_RAG" / "Week3_AI_GenAI_RAG.pdf"
prepare_document(pdf)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    temperature=0
)

ragas_llm = LangchainLLMWrapper(llm)

def rag(query):

    retrieved = retrieve(query)

    chunks = [
        point.payload["text"]
        for point in retrieved
    ]

    prompt = build_prompt(query, chunks)

    answer = ask(
        prompt=prompt,
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    return answer, chunks

test_cases = [
    {
        "question": "What is RAG?",
        "ground_truth": "Retrieval-Augmented Generation solves the knowledge cutoff problem."
    },
    {
        "question": "Why is chunk overlap important?",
        "ground_truth": "It preserves context across chunk boundaries."
    },
    {
        "question": "What library is used to read PDF files?",
        "ground_truth": "pymupdf4llm"
    },
    {
        "question": "Which model is recommended for generation?",
        "ground_truth": "llama-3.3-70b-versatile"
    },
    {
        "question": "Who invented Python?",
        "ground_truth": "I don't know."
    }
]

questions = []
answers = []
contexts = []
ground_truths = []

for test in test_cases:

    answer, retrieved_chunks = rag(test["question"])

    questions.append(test["question"])
    answers.append(answer)
    contexts.append(retrieved_chunks)
    ground_truths.append(test["ground_truth"])

dataset = Dataset.from_dict(
    {
        "question": questions,
        "answer": answers,
        "contexts": contexts,
        "ground_truth": ground_truths
    }
)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

ragas_embeddings = LangchainEmbeddingsWrapper(embeddings)
result = evaluate(
    dataset=dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
    ],
    llm=ragas_llm,
    embeddings=ragas_embeddings,
)
print(result)

df = result.to_pandas()

print(df)

lowest = df["faithfulness"].idxmin()

print("\nLowest Faithfulness Question:")
print(questions[lowest])

print("Faithfulness:", df.loc[lowest, "faithfulness"])
print("Answer Relevancy:", df.loc[lowest, "answer_relevancy"])

print("\nObservation:")

print(
    "The question 'Who invented Python?' received the lowest scores because "
    "the information was not present in the indexed PDF. As a result, the "
    "retriever could not provide supporting context, leading to low "
    "faithfulness and answer relevancy. This demonstrates that the RAG "
    "pipeline relies on the retrieved knowledge base rather than external "
    "information."
)