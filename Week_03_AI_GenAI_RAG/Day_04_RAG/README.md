# Day 04 – Retrieval-Augmented Generation (RAG)

This project introduces **Retrieval-Augmented Generation (RAG)**, a technique that combines **Large Language Models (LLMs)** with **vector databases** to generate grounded, context-aware answers from external documents.

A complete RAG pipeline was built using **Sentence Transformers**, **Qdrant**, **Groq (Llama 3.3 70B)**, and **PyMuPDF4LLM**. The project demonstrates how to load documents, split them into overlapping chunks, generate embeddings, store vectors in Qdrant, retrieve the most relevant chunks for a user query, augment the prompt with retrieved context, and generate answers grounded in the source document.

The project also includes reusable utility modules for document loading, chunking, retrieval, and prompt construction, making the RAG pipeline modular and easy to reuse.

---

## Topics Covered

* What is Retrieval-Augmented Generation (RAG)?
* Limitations of Large Language Models
* Knowledge cutoff and private data
* Complete RAG pipeline

  * Load
  * Chunk
  * Embed
  * Store
  * Retrieve
  * Augment Prompt
  * Generate
* Document loading using `pymupdf4llm`
* Text chunking with overlap
* Why chunk overlap improves retrieval

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
├── Day_03_Embeddings_Semantic_Search/
│   └── question_6/
│       └── utility_function.py
│
└── Day_04_RAG/
    │
    ├── Week3_AI_GenAI_RAG.pdf
    │
    ├── utils/
    │   ├── build_prompt.py
    │   ├── chunking.py
    │   ├── document_loader.py
    │   └── retrieval.py
    │
    ├── question_1/
    ├── question_2/
    ├── question_3/
    ├── question_4/
    ├── question_5/
    └── question_6/
```

---

## Tasks Completed

### Question 1 – Text Chunking

Implemented a reusable function:

```python
chunk_text(text, chunk_size=500, overlap=50)
```

The function:

* Splits a large document into fixed-size chunks.
* Preserves context using a 50-character overlap between consecutive chunks.
* Returns a list of overlapping text chunks.
* Tested the function on a PDF document and displayed the number of chunks generated.

---

### Question 2 – Document Loading, Embedding & Storage

Created a reusable document preparation pipeline.

The pipeline:

* Loads a PDF document using **PyMuPDF4LLM**.
* Converts the document into plain text.
* Splits the text into overlapping chunks.
* Creates metadata containing:

  * Source filename
  * Chunk index
* Generates embeddings using **Sentence Transformers**.
* Stores all chunks and metadata in **Qdrant**.

Reused the `embed_and_store()` utility created on **Day 03** to avoid duplicate code.

---

### Question 3 – Semantic Retrieval

Implemented a reusable function:

```python
retrieve(query, collection="chunks", top_k=3)
```

The function:

* Generates an embedding for the user query.
* Searches the Qdrant collection using cosine similarity.
* Retrieves the top-k most relevant chunks.
* Returns the retrieved chunk text for downstream use in the RAG pipeline.

---

### Question 4 – Prompt Augmentation

Implemented a reusable function:

```python
build_prompt(query, chunks)
```

The function:

* Inserts retrieved chunks as numbered context items.
* Appends the user's question.
* Adds a grounding instruction:

> Answer using only the context above. If the answer is not in the context, say: "I don't know."

This helps reduce hallucinations by constraining the model to the retrieved document context.

---

### Question 5 – Complete RAG Pipeline

Built an end-to-end Retrieval-Augmented Generation workflow by connecting all reusable components.

Pipeline:

```text
Document
      │
      ▼
Load PDF
      │
      ▼
Chunk Text
      │
      ▼
Generate Embeddings
      │
      ▼
Store in Qdrant
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Build Prompt
      │
      ▼
Groq (Llama 3.3-70B)
      │
      ▼
Grounded Answer
```

Asked three questions:

* A question answered by the document.
* Another question answered by the document.
* A question whose answer was absent from the document.

Verified that the model correctly responded:

```text
I don't know.
```

when the requested information was not present in the retrieved context.

---

### Question 6 – Hallucination Comparison

Compared the responses generated:

* Without RAG (raw Groq response)
* With RAG (retrieval-augmented response)

Using the same question.

Observed that:

* The raw LLM answered using its pre-trained knowledge.
* The RAG pipeline answered strictly from the retrieved document.
* When the information was unavailable in the document, the RAG system correctly replied **"I don't know"**, demonstrating improved grounding and reduced hallucinations.

---

## Reusable Utilities

Created reusable utility modules to simplify the RAG workflow:

* **chunking.py** – Splits documents into overlapping chunks.
* **document_loader.py** – Loads documents, chunks text, generates metadata, and stores vectors.
* **retrieval.py** – Retrieves the most relevant document chunks from Qdrant.
* **build_prompt.py** – Builds grounded prompts for the language model.

These utilities provide a modular foundation for building more advanced Retrieval-Augmented Generation systems in future projects.
