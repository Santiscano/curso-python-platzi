from fastapi import APIRouter, Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder

from config.database import Session
from middlewares.JWTBearer import JWTBearer
from entities.Movie import Movie
from services.movie import MovieServices

movie_router = APIRouter()

@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    # result = db.query(MovieModel).all()
    result = MovieServices(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000), q: str = None) -> Movie: # param id in path
    # la q serian los query parameters
    db = Session()
    # result = db.query(MovieModel).filter(MovieModel.id == id).first()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado la película"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]: # multiples query params
    db = Session()
    # result = db.query(MovieModel).filter(MovieModel.category == category).all()
    result = MovieServices(db).get_movies_by_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    # new_movie = MovieModel(**movie.model_dump())
    # db.add(new_movie)
    # db.commit()
    MovieServices(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})


@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie)-> dict:
    db = Session()
    # result = db.query(MovieModel).filter(MovieModel.id == id).first()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado la película"})
    
    # result.title = movie.title
    # result.overview = movie.overview
    # result.year = movie.year
    # result.rating = movie.rating
    # result.category = movie.category
    # db.commit()
    MovieServices(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado con exito la película"})

@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int)-> dict:
    db = Session()
    # result = db.query(MovieModel).filter(MovieModel.id == id).first()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado la película"})
    # db.delete(result)
    # db.commit()
    MovieServices(db).delete_movie(id)
    
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})
