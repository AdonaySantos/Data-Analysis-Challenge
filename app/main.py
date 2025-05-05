from contextlib import asynccontextmanager
import os, signal

from pymongo.cursor import Collection

from database.mongo import get_user_collection
from database.db_config import create_tables
from fastapi import FastAPI

from models.user import User, UserDict
from schemas.user import list_users

@asynccontextmanager
async def lifespan(_: FastAPI):
    print("Initializing..")
    create_tables()
    yield
    print("Finalizing")
    os.kill(os.getpid(), signal.SIGTERM)
    os.kill(os.getpid(), signal.SIGINT)

app = FastAPI(lifespan=lifespan)

@app.post("/users")
def post_users(users: list[User]):
    users_collection = get_user_collection()
    _ = users_collection.insert_many(users)
    return {"message": f"{len(users)} users inserted into MongoDB"}

@app.get("/superusers")
def get_superusers() -> dict[str, list[UserDict] | int]:
    collection: Collection[UserDict] = get_user_collection()
    superusers_cursor = collection.find({"score": { "$gte": 900}, "ativo": True})
    superusers = list_users(superusers_cursor)
    return {"superusers": superusers, "number of superusers": len(superusers)}

@app.get("/")
def hello():
    return "hello fucking world"
