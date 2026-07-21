# Write a build_prompt(query, chunks) function that inserts the retrieved chunks as numbered context items and appends: “Answer using only the context above. If the answer is not in the context, say: I don’t know.”

from pathlib import Path
import sys
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
from utils.build_prompt import build_prompt

chunks = [
    "Zero-shot prompting is a prompting technique where no examples are given.",
    "Few-shot prompting uses a small number of examples."
]
query = "What is zero-shot prompting?"
prompt = build_prompt(query, chunks)
print(prompt)