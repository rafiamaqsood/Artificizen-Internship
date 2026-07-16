# Call the API with llama-3.3-70b-versatile and llama-3.1-8b-instant for the same prompt. Print both responses and the usage.total_tokens for each. Note the difference in response quality and latency.

import time
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from wrapper_function import ask

prompt = "Explain Retrieval-Augmented Generation (RAG) in simple terms."

models = [
    "llama-3.1-8b-instant",
    "llama-3.3-70b-versatile"
]

for model in models:
    start = time.perf_counter()

    response = ask(
        prompt=prompt,
        model=model,
        system= "You are a strict JSON-only responder. Never output anything outside a JSON 
        return_response=True
    )

    end = time.perf_counter()

    print(f"Model: {model}\n")

    print(response.choices[0].message.content)

    print(f"\nTotal Tokens: {response.usage.total_tokens}")
    print(f"Latency: {end - start:.2f} seconds\n")