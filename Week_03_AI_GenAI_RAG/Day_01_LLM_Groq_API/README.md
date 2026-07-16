# Day 01 – Introduction to LLMs & Groq API

This project introduces the fundamentals of Large Language Models (LLMs) and demonstrates how to interact with Groq's inference API using Python. It covers secure API key management, model inference, prompt engineering basics, reusable wrapper functions, system prompts, and model comparison.

---

## Topics Covered

- AI, Machine Learning, Deep Learning, and Generative AI overview
- Introduction to Large Language Models (LLMs)
- Groq API setup and authentication
- Secure API key management using `.env`
- Chat Completions API
- Temperature parameter and response randomness
- System vs User prompts
- Wrapper function for reusable API calls
- Comparing different Groq models
- Measuring token usage and API latency

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
└── Day_01_LLM_Groq_API/
    ├── task1.py
    ├── task2.py
    ├── task3.py
    ├── task4.py
    ├── task5.py
    └── task6.py
```

---

## Tasks Completed

### Task 1 – Secure API Key Configuration

- Created a Groq account and generated an API key.
- Stored the API key securely in a `.env` file.
- Loaded the API key using **python-dotenv**.
- Verified the API key through `config.py`.

---

### Task 2 – First Groq API Call

- Connected to the Groq API.
- Used the **llama-3.1-8b-instant** model.
- Generated a response for:

> "Summarise what a transformer model does in 3 sentences."

---

### Task 3 – Temperature Comparison

Executed the same prompt:

- 3 times with **temperature = 0**
- 3 times with **temperature = 1.0**

Observation:

- **Temperature = 0** produced deterministic and nearly identical responses.
- **Temperature = 1.0** generated more diverse and creative responses.

---

### Task 4 – Reusable Wrapper Function

Implemented a reusable helper function:

```python
ask(
    prompt,
    system=None,
    model="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=512
)
```

Features:

- Optional system prompt
- Custom model selection
- Configurable temperature
- Configurable max tokens
- Exception handling
- Optional return of the complete API response for advanced use cases

This wrapper will be reused throughout Week 3.

---

### Task 5 – System Prompt

Used the following system instruction:

```
You are a strict JSON-only responder.
Never output anything outside a JSON object.
```

Verified that the model followed the system prompt by returning structured JSON output.

---

### Task 6 – Model Comparison

Compared two Groq-hosted models:

- `llama-3.1-8b-instant`
- `llama-3.3-70b-versatile`

Measured:

- Response quality
- Total token usage
- API latency

Observation:

- **llama-3.1-8b-instant**
  - Faster response time
  - Lower latency
  - Shorter responses

- **llama-3.3-70b-versatile**
  - Higher-quality responses
  - More detailed explanations
  - Slightly higher latency

---

## Technologies Used

- Python 3
- Groq Python SDK
- python-dotenv

---

## Key Concepts Learned

- What an LLM is
- Groq inference API
- Chat Completion API
- Prompt Engineering basics
- Temperature parameter
- System and User roles
- Secure API key management
- Wrapper function design
- Token usage
- API latency measurement
- Comparing LLM performance

---

## Learning Outcome

By completing Day 01, I learned how to securely connect to the Groq API, generate responses using different LLMs, control model behavior through prompts and temperature, build reusable API wrappers, and evaluate model performance based on response quality, token usage, and latency.