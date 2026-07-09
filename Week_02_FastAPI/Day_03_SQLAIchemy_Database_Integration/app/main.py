from fastapi import FastAPI

from .database import Base, engine
from .routers import users, posts

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Day 3")

app.include_router(users.router)
app.include_router(posts.router)