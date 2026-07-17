from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def ask(
    prompt,
    system=None,
    model="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=512,
    return_response=False,  
):
    try:
        messages = []

        if system:
            messages.append({
                "role": "system",
                "content": system
            })

        messages.append({
            "role": "user",
            "content": prompt
        })

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

        if return_response:
            return response

        return response.choices[0].message.content

    except Exception as e:
        print(f"Error calling Groq API: {e}")
        return None