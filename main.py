from fastapi import FastAPI

app = FastAPI()

message = {
    "status": "success",
    "message":"null"
}

@app.get("/")
async def root():
    return message

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}