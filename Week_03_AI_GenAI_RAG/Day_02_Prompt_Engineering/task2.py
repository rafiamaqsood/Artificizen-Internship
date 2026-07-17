# Write a zero-shot prompt that classifies a customer message as Complaint, Question, or Compliment. Test with five sample messages and print each classification.

import sys
from pathlib import Path
from groq import Groq

sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

messages = [
    "Are your laptop batteries long lasting?",
    "Your laptop batteries are not long lasting.",
    "Your laptops have very good battery life.",
    "Although I like the laptop's speed, the battery is not long lasting.",
    "I like the storage capacity of your laptop."
]

for i in messages:
    prompt = f""" Classify the following customer message into exactly one category:Complaint, Question,Compliment Examples:

Customer Message: "The laptop stopped working after one week."
Category: Complaint

Customer Message: "Do you offer a warranty on this laptop?"
Category: Question

Customer Message: "Your customer service was excellent!"
Category: Compliment

Now classify the following message.
Customer message: {i} 
Category: """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(f"Message: {i}")
    print(f"{response.choices[0].message.content}\n")