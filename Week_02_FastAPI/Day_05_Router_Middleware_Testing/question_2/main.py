# Add a middleware that logs every request method, path, and response status code to the console.

from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):

    print(f"Request: {request.method} {request.url.path}")
    response = await call_next(request)
    print(f"Response Status Code: {response.status_code}")

    return response

@app.get("/")
async def home():
    return {"message": "Welcome"}