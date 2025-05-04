from typing import Annotated
from fastapi import Depends
from fastapi.responses import JSONResponse
from pymongo.database import Database
from database.mongo import get_database
from schemas.user import UserSchema

class UserService:
    def user_register(self, json: list[UserSchema], sess) -> JSONResponse:
        try:
            users_collection = sess["users"]
            users_collection.insert_many(json)
            print("deu bom")
            return JSONResponse(status_code=200, content="deu bom")
        except Exception as e:
            print("deu ruim")
            return JSONResponse(status_code=500, content=f"deu ruim: {e}")

