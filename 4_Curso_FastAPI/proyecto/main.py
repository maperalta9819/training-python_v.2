from routers.variables import User
from fastapi import FastAPI
from fastapi.responses import HTMLResponse,JSONResponse
from utils.jwt_manager import create_token, validate_token
from fastapi.security.http import HTTPAuthorizationCredentials
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer
from routers.funciones import movie_router


app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

#GENERACION DE LOGUEO DE USER
@app.post('/login',tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token:str= create_token(user.dict())
    return JSONResponse(status_code=200,content=token)

app.include_router(movie_router)