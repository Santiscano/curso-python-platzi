from typing import List
from pydantic import BaseModel
from fastapi import APIRouter, Depends, Path, Query

food_router = APIRouter()

class Food(BaseModel):
    name: str
    description: List[str] = []


@food_router.post("/food/")
def prepare_food(orders: list[Food]):
    all_ingredients = []
    for food in orders:
        for ingredient in food.description:
            all_ingredients.append(ingredient)
            
    return {"ingredients": all_ingredients}