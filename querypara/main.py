from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
def get_items(
    name: str = Query(..., min_length=3, max_length=20),
    price: float = Query(..., gt=0, lt=10000)
):
    return {
        "name": name,
        "price": price
    }