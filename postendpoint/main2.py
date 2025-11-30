from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic Model
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.post("/items/")
def create_item(item: Item):
    return {
        "message": "Item created successfully!",
        "data": item
    }