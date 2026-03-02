from fastapi import FastAPI

# Create a FastAPI app instance
app = FastAPI()

# Define a path operation decorator for GET requests to the root URL ("/")
@app.get("/")
def read_root():
    """
    Handles GET requests to the root path and returns a JSON message.
    """
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """
    Handles GET requests to /items/{item_id} with a path parameter 
    (item_id) and an optional query parameter (q).
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}