from contextlib import asynccontextmanager
import os
import signal
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(_: FastAPI):
    print("Initializing..")
    yield
    print("Finalizing")
    os.kill(os.getpid(), signal.SIGTERM)
    os.kill(os.getpid(), signal.SIGINT)

app = FastAPI(lifespan=lifespan)

@app.get("/")
def hello():
    return { "Hello": "World" }
