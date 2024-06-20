from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

user = APIRouter()
users = [
    # {"id":1,"user":"mgarbett0","password":"mF2*Wc~f","created_at":"8/25/2023","status":False},
    # {"id":2,"user":"sscarre1","password":"yK2*(I?RJ)Pw.kPY","created_at":"7/22/2023","status":False},
    # {"id":3,"user":"gmilliken2","password":"zK7>gX@U<q+","created_at":"5/6/2024","status":True},
    # {"id":4,"user":"ihawkes3","password":"eH6_ISougz<xTG","created_at":"5/3/2024","status":True},
    # {"id":5,"user":"hschechter4","password":"gZ4.#~pXN(fmm3X","created_at":"5/20/2024","status":False}
]

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