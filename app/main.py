from contextlib import asynccontextmanager
import os, signal

from database.mongo import get_mongo
from database.db_config import create_tables
from fastapi import FastAPI

from models.user import User

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
    db = get_mongo()
    users_collection = db["users"]
    _ = users_collection.insert_many(users)
    return {"message": f"{len(users)} users inserted into MongoDB"}

@app.get("/")
def hello():
    return "hello fucking world"
