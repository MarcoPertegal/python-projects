from enum import Enum

import uvicorn
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from starlette import status
from typing import List
from pydantic import Field
from fastapi import Depends

from starlette.status import HTTP_201_CREATED

app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
def hellow_world():
    return 'aaaaa'


@app.get('/{id}', status_code=status.HTTP_200_OK)
def hellow_world2(id: int, parameter: str = 'hola'):
    return {'path': id, 'parameter': parameter}


class PeopleName(str, Enum):
    JUAN = 'JUAN'
    MARCO = 'MARCO'


PEOPLE = {
    PeopleName.JUAN: {
        "name": PeopleName.JUAN.value,
        "age": 23
    },
    PeopleName.MARCO: {
        "name": PeopleName.MARCO.value,
        "age": 22
    }
}


@app.get('/{name}', status_code=status.HTTP_200_OK)
def validate_person(name: PeopleName = Path(..., title='Nombre de la persona',
                                            description='Nombre de la persona que queremos validar'),
                    age: int = Query(10, gte=10, le=30, title='Person Age',
                                     description='Person age you want to find')):
    return {**PEOPLE[name], 'age_valid': PEOPLE[name]['age'] == age}


class Student(BaseModel):
    id: int
    name: str
    age: int = Field(..., le=18, ge=0)


class School(BaseModel):
    students: List[Student]


school = School(students=[])


@app.post('/student', response_model=School, status_code=HTTP_201_CREATED)
def create_student(student: Student) -> School:
    school.students.append(student)
    return school

def get_name(name: str) -> str:
    return name
@app.get("/student", response_model=List[Student])
def list_students(name: str = Depends(get_name)) -> List[Student]:
    return [student for student in school.students if student.name == name]