from typing import Union
from fastapi.responses import HTMLResponse
from fastapi import APIRouter


home_router = APIRouter()

@home_router.get("/", tags=["Home"])
def read_root():
    return {"Hello": "World"}


@home_router.get("/items/{item_id}") # http://localhost:8000/items/123?q=fastapi
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@home_router.get("/html")
def message_html():
    return HTMLResponse(content="<h1>Welcome to FastAPI</h1>", status_code=200)

