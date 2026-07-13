# Write at least three pytest tests using TestClient: one for a successful user creation, one for a duplicate email conflict, and one for a protected route returning 401 without a token.

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, Field

app = FastAPI()

users = []


class User(BaseModel):
    name: str
    email: str = Field(
        pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"
    )


@app.post("/users", status_code=201)
def create_user(user: User):

    # Check duplicate email
    for existing_user in users:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=409,
                detail="Email already exists"
            )

    users.append(user.model_dump())

    return {
        "message": "User created successfully",
        "user": user
    }


@app.get("/profile")
def profile(authorization: str | None = Header(default=None)):

    if authorization != "Bearer secret123":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    return {
        "message": "Welcome"
    }