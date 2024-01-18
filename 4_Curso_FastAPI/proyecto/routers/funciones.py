from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from typing import Optional,List
from models.movie import Movie as MovieModel
from Config.database import Session,engine,Base
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from routers.variables import MovieService
from routers.variables import Movie

movie_router = APIRouter()

#AGREGAR UNA PELICULA A LA LISTA
@movie_router.post('/movies/', tags=['movies'],response_model=dict,status_code=201)
def create_movie(movie:Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201,content={"message":"Se agrego la pelicula con exito"})

#OBTENER LISTA TOTAL DE PELICULAS
@movie_router.get('/movies', tags=['movies'],response_model=List[Movie],status_code=200,dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    results = MovieService(db).get_movies()
    return JSONResponse(status_code=200,content=jsonable_encoder(results))

#OBTENER UNA PELICULA POR SELECCION DE ID
@movie_router.get('/movies/{id}', tags=['movies'],response_model=List[Movie])
def get_movie(id: int = Path(ge=1,le=2000)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        JSONResponse(status_code=404,content={'message': 'No encontrado'})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

#OBTENER LISTA DE PELICULAS QUE CUMPLAN EL FILTRO
@movie_router.get('/movies/', tags=['movies'],response_model=List[Movie])
def get_movies_by_category(category: str= Query(min_length=4,max_length=500), year:int =Query(ge=1600,le=2024)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movie_by_category(category,year)
    if not result:
        return JSONResponse(status_code=404,content={'message':'Not found'})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

#MODIFICAR INFO DE PELICULA POR IDENTIFICACION DE ID
@movie_router.put('/movies/{id}', tags=['movies'],response_model=dict,status_code=200)
def put_movies(id:int,movie:Movie)-> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404,content={'message':'Not found'})
    MovieService(db).update_movie(id,movie)
    return JSONResponse(status_code=200,content={"message":"Se modifico la pelicula con exito"})

#ELIMINAR PELICULA IDENTIFICADA        
@movie_router.delete('/movies/{id}', tags=['movies'],response_model=dict,status_code=200)
def delete_movie(id:int)-> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404,content={'message':'Not found'})
    MovieService(db).delete_movie(result)
    return JSONResponse(status_code=200,content={'message':'Se elimino con exito'})