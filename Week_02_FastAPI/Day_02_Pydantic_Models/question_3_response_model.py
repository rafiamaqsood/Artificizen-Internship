# Create a UserRead model that adds an id: int field. Use response_model=UserRead on the route so the response always includes an id.


from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()
users=[]

class UserCreate(BaseModel):
    name: str
    email: str = Field(
        pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"
    )
    age: int =Field(ge=18 ,le=120)


class UserRead(UserCreate):
    id: int


@app.post("/users", response_model=UserRead)
def create_user(user: UserCreate):
    return {
        "id": 1,
        **user.model_dump()
    }
@app.get("/users")
def get_users():
    return users