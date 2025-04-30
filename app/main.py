from contextlib import asynccontextmanager
import os, signal
from database.db_config import create_tables
from fastapi import FastAPI

from routes.user_router import user_router

@asynccontextmanager
async def lifespan(_: FastAPI):
    print("Initializing..")
    create_tables()
    yield
    print("Finalizing")
    os.kill(os.getpid(), signal.SIGTERM)
    os.kill(os.getpid(), signal.SIGINT)

app = FastAPI(lifespan=lifespan)

app.include_router(user_router)

@app.get("/")
def hello():
    return { "Hello": "World" }
