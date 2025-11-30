from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

db = {}   # simple in-memory dictionary

# CREATE
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    db[item_id] = item
    return db[item_id]

# READ ONE
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return db.get(item_id, "Not found")

# READ ALL
@app.get("/items/")
def read_all():
    return db

# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    db[item_id] = item
    return db[item_id]

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return db.pop(item_id, "Not found")