from core.config_dotenv import DATABASE_URL
from pymongo import MongoClient
from models.user import User

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment variables.")

client: MongoClient[User] = MongoClient(DATABASE_URL)

def get_mongo():
    return client["json_users"]
