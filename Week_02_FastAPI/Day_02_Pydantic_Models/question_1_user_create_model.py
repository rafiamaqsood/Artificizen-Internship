# Define a UserCreate model with name: str, email: str, age: int. Create a POST /users route that accepts it and returns it back.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users=[]
class UserCreate(BaseModel):
    name: str
    email: str
    age: int


@app.post("/users")
def create_user(user: UserCreate):
    return user

@app.get("/users")
def get_users():
    return users