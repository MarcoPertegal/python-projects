from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel
#pydantic = creacion de dto

app = FastAPI()


@app.get("/")
async def get():
    return {"message": "Hello World"}
"""
class User(BaseModel):
    id: int
    name: str 
    fecha_alta = datetime | None
    aficiones = dict[str, PositiveInt]


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item"""