# Day 03 – Embeddings & Semantic Search

This project explores the fundamentals of **Embeddings**, **Semantic Search**, and **Vector Databases** using the `sentence-transformers` library with the **all-MiniLM-L6-v2** embedding model. It demonstrates how text can be converted into dense vector representations, compared using cosine similarity, and stored in vector databases such as **ChromaDB** and **Qdrant** for efficient semantic retrieval.

The project also introduces metadata filtering, vector storage, and reusable embedding utilities that will be used in the upcoming Retrieval-Augmented Generation (RAG) pipeline.

---

## Topics Covered

- What are embeddings?
- Semantic similarity using dense vectors
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Generating text embeddings
- Cosine similarity using NumPy
- Semantic search
- Vector databases
- ChromaDB
- Qdrant
- Payloads (metadata)
- Metadata filtering
- Batch embedding and storage

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
└── Day_03_Embeddings_Semantic_Search/
    ├── question_1/
    ├── question_2/
    ├── question_3/
    ├── question_4/
    ├── question_5/
    ├── question_6/
        └── utility_function.py
```

---

## Tasks Completed

### Question 1 – Sentence Embeddings & Cosine Similarity

Generated embeddings for six sentences using the **all-MiniLM-L6-v2** model.

Implemented cosine similarity manually using **NumPy** by computing:

- Dot product
- Vector magnitudes (L2 norm)
- Cosine similarity score

Compared every sentence pair and ranked them from the most similar to the least similar.

---

### Question 2 – Semantic Search

Implemented a reusable function:

```python
semantic_search(query, documents)
```

The function:

- Generates an embedding for the query.
- Generates embeddings for all documents.
- Computes cosine similarity between the query and each document.
- Sorts documents by similarity score.
- Returns the top 3 most semantically similar documents.

---

### Question 3 – Semantic Search with ChromaDB

Created an **in-memory ChromaDB** collection.

Completed the following tasks:

- Added 10 short paragraphs.
- Generated embeddings using Sentence Transformers.
- Stored document IDs, text, and embeddings.
- Queried the collection using a natural language question.
- Retrieved and displayed the top 2 most relevant paragraphs.

---

### Question 4 – Semantic Search with Qdrant

Repeated the previous exercise using **Qdrant** in in-memory mode.

Implemented:

- Collection creation
- Vector configuration
- Point insertion using `PointStruct`
- Payload storage
- Metadata filtering using the `source` field

Queried only documents where:

```text
source == "manual"
```

and displayed the top matching results.

---

### Question 5 – Semantic Search with Different Wording

Generated embeddings for 50 different sentences.

Queried the collection using a sentence that conveyed the same meaning using different wording.

Verified that semantic search successfully retrieved the correct sentence despite the absence of exact keyword matches.

---

### Question 6 – Reusable Embedding Utility

Created a reusable utility function:

```python
embed_and_store(texts, metadata_list, collection_name)
```

The function:

- Batch generates embeddings.
- Creates Qdrant `PointStruct` objects.
- Stores vectors together with metadata.
- Upserts all documents into a Qdrant collection.

This utility will be reused in the upcoming RAG pipeline for document ingestion.

---