from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from pydantic import BaseModel

app = FastAPI()


class Tractor(BaseModel):
    def __init__(id, self, marca, peso):
        self.id: int
        self.marca: str
        self.peso: float


tractor1 = Tractor(1, 'John Deere', 3.500)
tractor2 = Tractor(2, 'New Holland', 2600)

TRACTORES = [tractor1, tractor2]


@app.get('/tractor', response_model=Tractor, status_code=status.HTTP_200_OK)
async def getAll():
    return TRACTORES

