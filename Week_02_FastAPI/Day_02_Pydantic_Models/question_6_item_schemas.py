# Create both ItemCreate and ItemRead schemas for a product (name, price, in_stock). The read schema adds created_at. Use response_model to ensure created_at always appears in responses.

from pydantic import BaseModel, Field
from datetime import datetime
from fastapi import FastAPI

app= FastAPI()
items = []
class ItemCreate(BaseModel):
    name: str 
    price: float = Field(gt=0)
    in_stock: bool


class ItemRead(ItemCreate):
    created_at: datetime

@app.post("/items", response_model=ItemRead)
def create_item(item: ItemCreate):

    new_item = {
        **item.model_dump(),
        "created_at": datetime.now()
    }

    items.append(new_item)

    return new_item


@app.get("/items")
def get_items():
    return items