from fastapi import FastAPI
from uuid import uuid4, UUID
from typing import List
from fastapi import HTTPException
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
       # id = uuid4(),
        id = UUID("c1503dba-98fd-41d0-98d8-009eba917b86"),
        first_name = "Yakubu Seidu",
        last_name = "Bubaki",
        middle_name = "saed",
        gender = Gender.female,
        roles= [Role.student]

    ),
   User(
       # id = uuid4(),
       id = UUID("99f16d49-7b89-4ad8-af62-721fa1072cfb"),
        first_name = "Alexa",
        last_name = "Jones",
       middle_name = "June",
        gender = Gender.male,
        roles= [Role.admin, Role.user]

    ),
]

@app.get("/")
async def root():
    return {"Message":"Hello Africa"}

@app.get("/api/v1/fstarter")
async def fetch_users():
    return db;


@app.post("/api/v1/fstarter")
async def register_user(user:User):
    db.append(user)
    print(user.first_name)
    return {"id": user.id}


@app.delete("/api/v1/fstarter/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user_id == user.id:
            db.remove(user)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

