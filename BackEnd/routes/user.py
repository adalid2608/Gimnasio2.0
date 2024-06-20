from fastapi import APIRouter

user = APIRouter()
@user.get("/user")
def helloWorld():
    return "Hola 9b"