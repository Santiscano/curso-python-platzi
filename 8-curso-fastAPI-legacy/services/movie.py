from typing import List

from entities.Movie import Movie
from model.movie import Movie as MovieModel


class MovieServices:
    
    def __init__(self, db) -> None:
        self.db = db
    
    def get_movies(self) -> List[Movie]:
        return self.db.query(MovieModel).all()
    
    def get_movie(self, id: int) -> Movie:
        return self.db.query(MovieModel).filter(MovieModel.id == id).first()
    
    def get_movies_by_category(self, category: str) -> List[Movie]:
        return self.db.query(MovieModel).filter(MovieModel.category == category).all()
    
    def create_movie(self, movie: Movie) -> None:
        new_movie = MovieModel(**movie.model_dump()) # los ** son para desempaquetar el diccionario y pasar los valores como argumentos y con model_dump() se obtiene un diccionario con los valores del modelo
        self.db.add(new_movie)
        self.db.commit()
        
    def update_movie(self, id: int, movie: Movie) -> None:
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        result.title = movie.title
        result.overview = movie.overview
        result.year = movie.year
        result.rating = movie.rating
        result.category = movie.category
        self.db.commit()
        
    def delete_movie(self, id: int) -> None:
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        self.db.delete(result)
        self.db.commit()