import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Fruit(BaseModel):
    name: str
    
class Fruits(BaseModel):
    fruits: List[Fruit]

memory_db = {"fruits": []}

@app.get("/fruits", response_model=Fruits)
async def get_fruits():
    return Fruits(fruits=memory_db["fruits"])

@app.post("/fruits", response_model=Fruits)
async def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return Fruits(fruits=memory_db["fruits"])



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)