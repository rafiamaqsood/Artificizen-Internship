from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

    model_config = {
        "from_attributes": True
    }

class PostCreate(BaseModel):
    title: str
    content: str
    owner_id: int

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int

    model_config = {
        "from_attributes": True
    }