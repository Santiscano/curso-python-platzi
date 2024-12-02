from fastapi import APIRouter
from fastapi.responses import JSONResponse

from entities.User import User
from jwt_manager import create_token


auth_router = APIRouter()

@auth_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        # token: str = create_token(user.dict()) # dict() convierte el objeto a diccionario - !deprecated
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)

