from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

user = APIRouter()
users = []

class UsersModel(BaseModel):
    id: str
    user: str
    password: str
    crated_at: datetime = datetime.now()
    status: bool = False

@user.get("/")
def welcome():
    return "Hola 9b"

@user.get("/users")
def get_users():
    return users

@user.post("/users")
def save_users(userInsert:UsersModel):
    users.append(userInsert)
    return "Datos Almacenados correctamente"