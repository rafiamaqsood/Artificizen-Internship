import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import GROQ_API_KEY 
from groq import Groq


client = Groq(api_key=GROQ_API_KEY)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Summarise what a transformer model does in 3 sentences"
        }
    ]
)

print(response.choices[0].message.content)