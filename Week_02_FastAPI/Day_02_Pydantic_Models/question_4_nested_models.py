# Create a nested model: Address with city and country, and embed it in a UserCreate model.

from pydantic import BaseModel , Field
from fastapi import FastAPI

app = FastAPI()
users=[]

class Address(BaseModel):
    city: str
    country: str

class UserCreate(BaseModel):
    name: str
    email: str = Field(
        pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"
    )
    age: int =Field(ge=18 ,le=120)
    address :Address

@app.post("/users")
def create_user(user: UserCreate):
    return user

@app.get("/users")
def get_users():
    return users