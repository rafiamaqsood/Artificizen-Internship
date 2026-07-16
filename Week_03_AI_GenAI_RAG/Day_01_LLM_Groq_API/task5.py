# Pass a system message: “You are a strict JSON-only responder. Never output anything outside a JSON object.” Ask any question and print the raw output. Did it obey?

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from wrapper_function import ask

response = ask(
    prompt="Explain Retrieval-Augmented Generation (RAG) in simple terms.",
    system="You are a strict JSON-only responder. Never output anything outside a JSON object."
)
print(response)