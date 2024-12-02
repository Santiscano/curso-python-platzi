from fastapi import FastAPI

from config.database import engine, Base
from middlewares.error_handler import ErrorHandler

from routers.movies import movie_router
from routers.auth import auth_router
from routers.home import home_router


app = FastAPI()
app.title = "My First FastAPI App"
app.version = "0.0.1"
app.description = "This is my first FastAPI app. It is a simple example of how to use FastAPI."

app.add_middleware(ErrorHandler)

app.include_router(home_router)
app.include_router(auth_router)
app.include_router(movie_router)

Base.metadata.create_all(bind=engine)








