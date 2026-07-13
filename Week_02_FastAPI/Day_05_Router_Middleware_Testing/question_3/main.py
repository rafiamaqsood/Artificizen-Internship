# Add CORSMiddleware configured to allow requests from http://localhost:3000 only.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI ()

origins=[
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods =["*"],
    allow_headers =["*"]

)

@app.get("/")
async def home():
    return {"message": "CORS Enabled"}