# Add a @field_validator to reject any name that contains numbers.

from pydantic import BaseModel , Field, field_validator
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

    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        for i in value:
            if i.isdigit():
                raise ValueError("Name cannot contain numbers")
        return value


@app.post("/users")
def create_user(user: UserCreate):
    return user
@app.get("/users")
def get_users():
    return users