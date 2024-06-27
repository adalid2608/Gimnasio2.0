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

@user.get("/", tags=["Inicio"])
def welcome():
    return "Hola 9b"

@user.get("/users",tags=["Usuarios"])
def get_users():
    return users

@user.post("/users/{user_id}",tags=["Usuarios"])
def get_persons(user_id:str):
    for user in users:
        if user.id == user_id:
            return user
    return {"message": f"NO existe el registro"}

@user.post("/users/",tags=["Usuarios"])
def save_users(userInsert:UsersModel):
    users.append(userInsert)
    return "Datos Almacenados correctamente"

@user.put("/users/{user_id}",tags=["Usuarios"])
def updateUser(update_user:UsersModel, user_id:str):
    for index, user in enumerate(users):
        if user.id == user_id:
            update_user.crated_at = user.crated_at
            users[index] = update_user
            return {"message": f"Se ah modificado un usuario con el Id: {user_id}"}
        
@user.delete("/users/{user_id}",tags=["Usuarios"])
def delete_user(user_id:str):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {"message": f"Se ah eliminado un usuario con el Id: {user_id}"}