from typing import Annotated

from fastapi import Depends, FastAPI
from sqlmodel import Session, create_engine, SQLModel

sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

engine_sqlite = create_engine(sqlite_url, echo=True)

def create_all_tables(app:FastAPI):
    SQLModel.metadata.create_all(engine_sqlite)
    yield


def get_session():
    with Session(engine_sqlite) as session:
        yield session



SessionDep = Annotated[Session, Depends(get_session)]