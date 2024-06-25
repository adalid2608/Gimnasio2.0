from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

person = APIRouter()
persons = []

class PersonsModel(BaseModel):
    id: str
    user: str
    password: str
    crated_at: datetime = datetime.now()
    status: bool = False

@person.get("/persons")
def get_persons():
    return persons

@person.post("/persons")
def save_persons(personInsert:PersonsModel):
    persons.append(personInsert)
    return "Datos Almacenados correctamente"