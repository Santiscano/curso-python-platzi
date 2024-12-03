from fastapi import FastAPI

from app.routers.time_example import time_router
from app.routers.customer import customer_router
from app.routers.transactions import router as transaction_router
from config.db_sqlite import create_all_tables

app = FastAPI(lifespan=create_all_tables)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(time_router)
app.include_router(customer_router)
app.include_router(transaction_router)
