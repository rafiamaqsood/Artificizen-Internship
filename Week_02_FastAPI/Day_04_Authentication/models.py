from sqlalchemy import Column ,Integer, String
from database import Base
from pydantic import BaseModel

class User(Base):

    __tablename__ = "user_1"

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="user", nullable=False)

class UserRegister(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str