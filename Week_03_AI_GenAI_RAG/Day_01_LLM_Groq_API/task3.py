import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

prompt = "Summarise what a transformer model does in 3 sentences"

print("Temperature = 0")

for i in range(1, 4):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(f"\nResponse {i}:")
    print(response.choices[0].message.content)

print("\n")
print("Temperature = 1.0")

for i in range(1, 4):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=1.0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    print(f"\nResponse {i}:")
    print(response.choices[0].message.content)