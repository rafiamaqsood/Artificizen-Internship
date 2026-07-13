from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app):
    print("Application Started")
    yield
    print("Application Stopped")

app = FastAPI(lifespan=lifespan)