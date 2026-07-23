from app.config import GROQ_API_KEY , MODEL_NAME
from groq import Groq

client = Groq(api_key=GROQ_API_KEY)

def ask_groq(prompt):
    response = client.chat.completions.create(
        model= MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return (response.choices[0].message.content)

def ask_groq_stream(prompt):
    stream = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=True
    )
    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content