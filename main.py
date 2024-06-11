from fastapi import FastAPI

app = FastAPI()

message = {
    "status": "success",
    "message":"root domain"
}

@app.get("/")
async def root():
    return message

@app.get("/weather")
async def weather():
    return {"message": "weather end point"}

@app.get("/marine")
async def marine():
    return {"message": "marine end point"}

@app.get("/coal")
async def coal():
    return {"message": "coal end point"}

@app.get("/geopolitics")
async def geopolitics():
    return {"message": "geopolitics end point"}