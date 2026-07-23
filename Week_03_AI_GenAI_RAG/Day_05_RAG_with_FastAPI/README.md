# Day 05 – RAG with FastAPI + Multi-Turn Chat + Evaluation

This project extends the Retrieval-Augmented Generation (RAG) pipeline built on **Day 04** by exposing it as a **FastAPI** application and adding production-oriented features such as **multi-turn conversations**, **response caching**, **streaming responses**, and **RAG evaluation**.

The application allows users to query a document through a REST API, retrieves the most relevant document chunks from **Qdrant**, augments the prompt with retrieved context, and generates grounded answers using **Groq (Llama 3.3 70B)**.

Additional improvements include maintaining conversation history for follow-up questions, caching repeated queries using **MD5 hashing**, streaming responses token-by-token, performing manual evaluation using predefined test cases, and evaluating the RAG pipeline using **Ragas** with **Faithfulness** and **Answer Relevancy** metrics.

---

## Topics Covered

* Building REST APIs with FastAPI
* Exposing the RAG pipeline through `POST /chat`
* Returning source citations with chunk metadata
* Multi-turn conversations using chat history
* Context window management
* Streaming responses with `StreamingResponse`
* Query caching using `hashlib.md5`
* Manual RAG evaluation
* Automated RAG evaluation using Ragas
* Faithfulness and Answer Relevancy metrics
* Using HuggingFace embeddings for Ragas evaluation
* Production considerations for RAG applications

---

## Project Structure

```text
Week_03_AI_GenAI_RAG/
│
├── .env
├── .gitignore
├── config.py
├── wrapper_function.py
│
├── Day_04_RAG/
│   ├── Week3_AI_GenAI_RAG.pdf
│   └── utils/
│       ├── build_prompt.py
│       ├── chunking.py
│       ├── document_loader.py
│       └── retrieval.py
│
└── Day_05_RAG_with_FastAPI/
    │
    ├── question_1.py
    ├── question_2.py
    ├── question_3.py
    ├── question_4.py
    ├── question_5.py
    └── question_6.py
```

---

## Tasks Completed

### Question 1 – Expose the RAG Pipeline with FastAPI

Wrapped the Day 04 RAG pipeline inside a FastAPI application.

Implemented a REST endpoint:

```http
POST /chat
```

Request:

```json
{
    "query": "What is RAG?"
}
```

Response:

```json
{
    "answer": "...",
    "sources": [
        {
            "source": "Week3_AI_GenAI_RAG.pdf",
            "chunk_index": 3,
            "score": 0.91
        }
    ]
}
```

The API:

* Retrieves relevant document chunks.
* Builds a grounded prompt.
* Generates an answer using Groq.
* Returns both the generated answer and chunk metadata used as evidence.

---

### Question 2 – Multi-Turn Conversation

Added support for conversational memory.

Implemented:

```python
conversation_history = {}
```

where each session stores:

```python
[
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
]
```

Features:

* Separate history for each session ID.
* Stores the last six conversation turns.
* Passes previous messages to Groq for follow-up questions.
* Trims older messages to prevent the context window from growing indefinitely.

---

### Question 3 – Query Caching

Implemented an in-memory cache to avoid regenerating answers for repeated queries.

Each query is hashed using:

```python
hashlib.md5(query.encode()).hexdigest()
```

The cache stores:

* Generated answer
* Retrieved source metadata

When the same query is requested again:

* Cached response is returned immediately.
* Retrieval and LLM generation are skipped.
* Cache hits and cache misses are logged.

---

### Question 4 – Streaming Responses

Implemented token streaming using:

```python
StreamingResponse
```

and Groq's

```python
stream=True
```

Instead of waiting for the complete answer, tokens are streamed progressively to the client.

Features:

* Real-time token generation.
* Lower perceived latency.
* Conversation history updated after streaming completes.
* Cached responses returned immediately on repeated queries.

---

### Question 5 – Manual Evaluation

Prepared five question–answer test cases based on the indexed document.

Each generated answer was compared against an expected answer and classified as:

* Correct
* Partially Correct
* Wrong

Calculated an overall accuracy percentage for the RAG pipeline.

This manual evaluation provides a quick way to verify retrieval quality and answer correctness.

---

### Question 6 – Automated Evaluation with Ragas

Installed and configured **Ragas** to evaluate the RAG pipeline.

Created a dataset containing:

* Questions
* Generated answers
* Retrieved contexts
* Ground-truth answers

Evaluated using:

* Faithfulness
* Answer Relevancy

Since Groq was used instead of OpenAI:

* Configured `ChatGroq` as the evaluation LLM.
* Used HuggingFace Sentence Transformers embeddings wrapped with:

```python
LangchainEmbeddingsWrapper
```

Printed:

* Overall Faithfulness score
* Overall Answer Relevancy score
* Individual scores for every test case
* Lowest-scoring question

Observed that the question:

```text
Who invented Python?
```

received the lowest score because the information was not contained in the indexed document, demonstrating that the RAG pipeline remains grounded in retrieved context rather than relying on external model knowledge.

---