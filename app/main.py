from contextlib import asynccontextmanager
import os
import signal

from fastapi.responses import JSONResponse

from database.mongo import get_user_collection
from database.db_config import create_tables
from fastapi import FastAPI, Request

from models.user import User
from services.user_services import get_all_superusers, get_all_top_countries, get_team_insights


@asynccontextmanager
async def lifespan(_: FastAPI):
    print("Initializing..")
    create_tables()
    yield
    print("Finalizing")
    os.kill(os.getpid(), signal.SIGTERM)
    os.kill(os.getpid(), signal.SIGINT)

app = FastAPI(lifespan=lifespan)


@app.exception_handler(Exception)
async def exception_handler(_: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": exc},
    )


@app.post("/users")
def post_users(users: list[User]):
    try:
        users_collection = get_user_collection()
        documents = [user.model_dump(by_alias=True) for user in users]
        _ = users_collection.insert_many(documents)
    except Exception as e:
        return {"error": f"Error while insert: {e}"}
    return {"message": f"{len(users)} users inserted into MongoDB"}


@app.delete("/delete-all")
def delete_all():
    try:
        collection = get_user_collection()
        _ = collection.delete_many({})
    except Exception as e:
        return {"error": f"Error deleting all: {e}"}
    return {"message": "All users deleted"}


@app.get("/superusers")
def get_superusers():
    sups = get_all_superusers()
    return {
        "superusers": sups,
        "number of superusers": len(sups) if isinstance(sups, list) else 0
    }


@app.get("/top-countries")
def get_users_by_country() -> list[dict[str, str | int]]:
    top_countries = get_all_top_countries()
    return top_countries if top_countries else [{}]


@app.get("/team-insights")
def get_all_insights() -> list[dict[str, str | int]]:
    team_insights = get_team_insights()
    return team_insights


@app.get("/")
def hello():
    return "hello fucking world"
