from typing import Any
from core.config_dotenv import DATABASE_URL
from pymongo import MongoClient

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment variables.")

client: MongoClient[Any] = MongoClient(DATABASE_URL)


def get_user_collection():
    return client["json_users"]["users"]
