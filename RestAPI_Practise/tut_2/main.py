# step 1: import FastAPI
from fastapi import FastAPI

from typing import List
from model import User, Gender, Role
from uuid import uuid4, UUID

# step2: create a fastAPI instance
app = FastAPI()

food_items = {
    'Indian': ["Dosa", "Idly"],
    'American': ['Burger', 'Pizza'],
    'Mexican': ['Taco', 'Burrito']
}

# Invoking DB
db: List[User] = [
    User(
        id=uuid4(),
        first_name="Shubham",
        last_name="Rathod",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Gibbo",
        last_name="Rathod",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]


# path operation decorator
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/get_items/{cusine}")
async def get_items(cusine):
    return food_items.get(cusine)


@app.get("/api/v1/user")
async def fetch_user():
    return db


@app.post("/api/v1/user")
async def register_user(user: User):
    db.append(user)
    return {"user id" : user.id}

@app.delete("/api/v1/user/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return

