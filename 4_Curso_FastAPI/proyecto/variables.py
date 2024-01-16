#LIBRERIAS USADAS DENTRO DE MAIN


#LIBRERIAS USADAS DENTRO DE VARIABLES
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Any, Coroutine, Optional,List
from fastapi.security import HTTPBearer
from fastapi import HTTPException
from jwt_manager import validate_token
from starlette.requests import Request
from Config.database import Session,engine,Base
from models.movie import Movie as MovieModel

Base.metadata.create_all(bind=engine)


class JWTBearer(HTTPBearer):
      async def __call__(self, request: Request):
            auth = await super().__call__(request)
            data = validate_token(auth.credentials)
            if data['email'] != "admin@gmail.com":
                 raise HTTPException(status_code=403,detail="Invalid Credentials") 

class User(BaseModel):
    email:str
    password:str

class Movie(BaseModel):
    id:Optional[int] = None
    title:str =Field(min_length=2,max_length=90)
    overview:str=Field(min_length=2,max_length=150)
    year:int=Field(le=2024)
    rating:float=Field(ge=0,le=10)
    category:str=Field(min_length=2,max_length=90)

    class Config:
        schema_extra = {
            "example":{
                "id": 1,
                "title": "Ingresa tu peli",
                "overview": "Ingresa tu resumen",
                "year": "2024",
                "rating": 9.8,
                "category":"Ingresa la categoria"
            }
        }

movies = [{
        "id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
    },
    {
        "id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
    }      
]

