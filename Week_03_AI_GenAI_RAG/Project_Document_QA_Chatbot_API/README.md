# 📄 Document QA Chatbot API

A **Retrieval-Augmented Generation (RAG)** based Document Question Answering API built with **FastAPI**, **Sentence Transformers**, **FAISS**, and **Groq LLM**. Upload PDF documents, ask questions about their content, and receive accurate answers grounded in the uploaded document.

---

# Project Structure

```
Project_Document_QA_Chatbot_API/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── utils/
│   ├── config.py
│   └── main.py
│
├── tests/
├── uploads/
├── requirements.txt
├── .env
└── README.md
```

---

# Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd Project_Document_QA_Chatbot_API
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
COLLECTION_NAME=document_QA_chatbot_chunks
MODEL_NAME=llama-3.3-70b-versatile
EMBEDDING_MODEL=all-MiniLM-L6-v2
```

## 5. Run the application

```bash
uvicorn app.main:app --reload
```

Server starts at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# How to Ingest a Document

Use the `/ingest/` endpoint to upload a PDF document.

### Using Swagger UI

1. Open:

```
http://127.0.0.1:8000/docs
```

2. Expand **POST /ingest/**

3. Click **Try it out**

4. Choose a PDF file.

5. Click **Execute**

Example successful response:

```json
{
  "message": "Document ingested successfully."
}
```

---


# How to Query the Document

After ingesting a document, use the `/chat/` endpoint.

---

# Streaming Responses

Use the streaming endpoint:

```
POST /chat/stream
```


---

# Running Tests

Run all tests:

```bash
python -m pytest
```

Example output:

```
============================= test session starts =============================

tests/test_cache.py .....
tests/test_chat.py .....
tests/test_ingest.py .....
tests/test_no_answer.py .....
tests/test_sources.py .....

========================= 5 passed in XX.XX seconds =========================
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Home   |
| POST | `/ingest/` | Upload and index a PDF document |
| POST | `/chat/` | Ask questions about the uploaded document |
| POST | `/chat/stream` | Stream generated responses |

---

# RAG Pipeline

```
PDF
   │
   ▼
Extract Text
   │
   ▼
Chunk Text
   │
   ▼
Generate Embeddings
   │
   ▼
Store in FAISS
   │
   ▼
User Question
   │
   ▼
Semantic Search
   │
   ▼
Retrieved Context
   │
   ▼
Groq LLM
   │
   ▼
Final Answer
```

---