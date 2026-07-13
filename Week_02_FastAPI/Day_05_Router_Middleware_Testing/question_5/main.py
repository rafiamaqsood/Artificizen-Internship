# Add a background task to the POST /users route that “sends a welcome email” (just print it) without blocking the response.

from fastapi import FastAPI,BackgroundTasks

app= FastAPI()

def send_email():
    print("sends a welcome email")

@app.post("/register")
def register(background_tasks:BackgroundTasks):
    background_tasks.add_task(send_email)
    return {
        "message": "Registration successful"
    }