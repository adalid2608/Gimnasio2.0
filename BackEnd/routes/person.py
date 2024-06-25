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

@person.get("/persons",tags=["Personas"])
def get_persons():
    return persons

@person.post("/persons/{person_id}",tags=["Personas"])
def get_persons(person_id:str):
    for person in persons:
        if person.id == person_id:
            return person
    return {"message": f"NO existe el registro"}

@person.post("/persons/",tags=["Personas"])
def save_persons(personInsert:PersonsModel):
    persons.append(personInsert)
    return "Datos Almacenados correctamente"

@person.put("/persons/{person_id}",tags=["Personas"])
def updateUser(update_person:PersonsModel, person_id:str):
    for index, person in enumerate(persons):
        if person.id == person_id:
            update_person.crated_at = person.crated_at
            persons[index] = update_person
            return {"message": f"Se ah modificado una persona con el Id: {person_id}"}

@person.delete("/persons/{person_id}",tags=["Personas"])
def delete_user(person_id:str):
    for index, person in enumerate(persons):
        if person.id == person_id:
            persons.pop(index)
            return {"message": f"Se ah eliminado una persona con el Id: {person_id}"}