from variables import movies, User, Movie, JWTBearer
from fastapi import FastAPI, Body, Path, Query, Depends
from fastapi.responses import HTMLResponse,JSONResponse
from typing import List
from jwt_manager import create_token
from fastapi.security.http import HTTPAuthorizationCredentials
from Config.database import Session,engine,Base
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder


app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

#GENERACION DE LOGUEO DE USER
@app.post('/login',tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token:str= create_token(user.dict())
    return JSONResponse(status_code=200,content=token)

#AGREGAR UNA PELICULA A LA LISTA
@app.post('/movies/', tags=['movies'],response_model=dict,status_code=201)
def create_movie(movie:Movie) -> dict:
    db = Session()
    new_movie = MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201,content={"message":"Se agrego la pelicula con exito"})

#OBTENER LISTA TOTAL DE PELICULAS
@app.get('/movies', tags=['movies'],response_model=List[Movie],status_code=200,dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    results = db.query(MovieModel).all()
    return JSONResponse(status_code=200,content=jsonable_encoder(results))

#OBTENER UNA PELICULA POR SELECCION DE ID
@app.get('/movies/{id}', tags=['movies'],response_model=List[Movie])
def get_movie(id: int = Path(ge=1,le=2000)) -> List[Movie]:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        JSONResponse(status_code=404,content={'message': 'No encontrado'})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

#OBTENER LISTA DE PELICULAS QUE CUMPLAN EL FILTRO
@app.get('/movies/', tags=['movies'],response_model=List[Movie])
def get_movies_by_category(category: str= Query(min_length=4,max_length=500), year:int =Query(ge=1600,le=2024)) -> List[Movie]:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.category == category or MovieModel.year == year).all()
    if not result:
        return JSONResponse(status_code=404,content={'message':'Not found'})
    #data = [ item for item in movies if item['year'] == str(year) and item["category"] == category]
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

#MODIFICAR INFO DE PELICULA POR IDENTIFICACION DE ID
@app.put('/movies/{id}', tags=['movies'],response_model=dict,status_code=200)
def put_movies(id:int,movie:Movie)-> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404,content={'message':'Not found'})
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category
    db.commit()
    return JSONResponse(status_code=200,content={"message":"Se modifico la pelicula con exito"})

#ELIMINAR PELICULA IDENTIFICADA        
@app.delete('/movies/{id}', tags=['movies'],response_model=dict,status_code=200)
def delete_movie(id:int)-> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404,content={'message':'Not found'})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200,content={'message':'Se elimino con exito'})


    