#LIBRERIAS USADAS DENTRO DE VARIABLES
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from fastapi.security import HTTPBearer
from fastapi import HTTPException
from utils.jwt_manager import create_token, validate_token
from starlette.requests import Request
from Config.database import Session,engine,Base
from models.movie import Movie as MovieModel
from typing import Optional

Base.metadata.create_all(bind=engine)

class Movie(BaseModel):
    id:Optional[int] = None
    title:str =Field(min_length=2,max_length=90)
    overview:str=Field(min_length=2,max_length=150)
    year:int=Field(le=2024)
    rating:float=Field(ge=0,le=10)
    category:str=Field(min_length=2,max_length=90)
    class Config:
        json_schema_extra = {
            "example":{
                "id": 1,
                "title": "Ingresa tu peli",
                "overview": "Ingresa tu resumen",
                "year": "2024",
                "rating": 9.8,
                "category":"Ingresa la categoria"
            }
        }

class MovieService():
    def __init__(self,db) -> None:
        self.db = db
    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    def get_movie(self,id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    def get_movie_by_category(self,category,year):
         result = self.db.query(MovieModel).filter(MovieModel.category == category or MovieModel.year == year).all()
         return result
    def create_movie(self,movie:Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return 
    def update_movie(self,id:int,data:Movie):
         movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
         movie.title = data.title
         movie.overview = data.overview
         movie.year = data.year
         movie.rating = data.rating
         movie.category = data.category
         self.db.commit()
         return
    def delete_movie(self,movie:Movie):
         self.db.delete(movie)
         self.db.commit()
         return

         
         
class JWTBearer(HTTPBearer):
      async def __call__(self, request: Request):
            auth = await super().__call__(request)
            data = validate_token(auth.credentials)
            if data['email'] != "admin@gmail.com":
                 raise HTTPException(status_code=403,detail="Invalid Credentials") 

class User(BaseModel):
    email:str
    password:str

"""informacion que se usaba para la etapa de testeo antes de insertar la base de datos:
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
"""


