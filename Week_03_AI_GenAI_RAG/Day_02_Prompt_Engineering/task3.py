# Ask Groq to solve a logic puzzle. Run it once without CoT, then add “Think step by step” at the end. Print both answers and note whether CoT helped.

import sys
from pathlib import Path
from groq import Groq

sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

puzzle = """
A farmer has 17 sheep.
All but 9 die.
How many sheep are left?
"""

response1 = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": puzzle
        }
    ]
)

response2 = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": puzzle + "\n\nThink step by step."
        }
    ]
)

print("=== Without CoT ===")
print(response1.choices[0].message.content)

print("\n=== With CoT ===")
print(response2.choices[0].message.content)