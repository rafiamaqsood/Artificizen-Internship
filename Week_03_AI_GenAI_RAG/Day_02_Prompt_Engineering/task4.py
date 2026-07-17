# Write a system prompt that turns the model into a senior Python code reviewer: strict, concise, no praise, actionable suggestions only. Submit a buggy code snippet and compare to a default system prompt output.

import sys
from pathlib import Path
from groq import Groq

sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

code = """
def divide(a, b):
    print(a / b)

divide("rafia", 100)
"""

default_response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": f"Review the following Python code:\n\n{code}"
        }
    ]
)

review_response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": """
You are a senior Python code reviewer.

Rules:
- Be strict.
- Be concise.
- Do not praise the code.
- Provide only actionable suggestions.
- Focus on correctness, readability, performance, and Python best practices.
- Do not rewrite the entire program unless necessary.
"""
        },
        {
            "role": "user",
            "content": f"Review the following Python code:\n\n{code}"
        }
    ]
)

print("===== Default Output =====")
print(default_response.choices[0].message.content)

print("\n===== Senior Reviewer Output =====")
print(review_response.choices[0].message.content)