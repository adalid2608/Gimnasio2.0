from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

user = APIRouter()
usersInfo = []

class usersModel(BaseModel):
    id: str
    user: str
    password: str
    crated_at: datetime = datetime.now
    status: bool = False

@user.get("/")
def bienvenida():
    return "Hola 9b"

@user.get("/user")
def usuarios():
    return "Lista de Usuarios"