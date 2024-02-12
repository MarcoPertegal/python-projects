from typing import List
from typing import Annotated

from fastapi import Depends, FastAPI, Path, HTTPException, Body
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

#Con el passwordBearer me pide una contraseña y un usuario
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Tractor(BaseModel):
    id: int
    marca: str
    peso: float


tractor1 = Tractor(id=1, marca='John Deere', peso=3.500)
tractor2 = Tractor(id=2, marca='New Holland', peso=2600)


class EditTractorDto(BaseModel):
    id: int
    marca: str
    peso: float


class TractorDtoResponse(BaseModel):
    id: int
    marca:str
    peso: float


TRACTORES = [tractor1, tractor2]


@app.get('/tractor', response_model=List[Tractor], status_code=status.HTTP_200_OK)
async def getAll(token: Annotated[str, Depends(oauth2_scheme)]):
    return TRACTORES


@app.get('/tractor/{id}', response_model=Tractor, status_code=status.HTTP_200_OK)
async def getById(id: int = Path(..., title='id del tractor')):
    for tractor in TRACTORES:
        if tractor.id == id:
            return tractor
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tractor not found")


@app.post('/tractor', response_model=Tractor, status_code=status.HTTP_201_CREATED)
async def createTractor(newTractor: EditTractorDto = Body(..., title='nuevo tractor')):
    for existing_tractor in TRACTORES:
        if existing_tractor.id == newTractor.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tractor with this id already exists")
    created_tractor = Tractor(
        id=newTractor.id,
        marca=newTractor.marca,
        peso=newTractor.peso
    )
    TRACTORES.append(created_tractor)
    return TractorDtoResponse(id=created_tractor.id, marca=created_tractor.marca, peso=created_tractor.peso)
    #Si quiero que el dto no devuelva lo mismo que los atritutos que tiene la clase Tractor como por ejemplo el id me da error 500

@app.put('/tractor', response_model=Tractor, status_code=status.HTTP_200_OK)
async def editTractor(editedTractor: EditTractorDto = Body(..., title='Tractor editado')):
    for existing_tractor in TRACTORES:
        if existing_tractor.id == editedTractor.id:
            updated_tractor = Tractor(
                id=editedTractor.id,
                marca=editedTractor.marca,
                peso=editedTractor.peso
            )
            TRACTORES.remove(existing_tractor)
            TRACTORES.append(updated_tractor)
            return TractorDtoResponse(id=updated_tractor.id, marca=updated_tractor.marca, peso=updated_tractor.peso)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tractor not found")


@app.delete('/tractor/{id}')
async def deleteTractor(id: int = Path(..., title='id del tractor')):
    for existing_tractor in TRACTORES:
        if existing_tractor.id == id:
            TRACTORES.remove(existing_tractor)
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Tractor deleted")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tractor not found")