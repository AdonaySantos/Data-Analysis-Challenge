from typing import Annotated
from fastapi import APIRouter, Depends

from database.connection import get_db
from sqlalchemy.orm import Session
from models.users import User
from schemas.user import UserSchema
from services.user_service import UserService

user_router = APIRouter(prefix="/users")

@user_router.post("/register")
def data_register(json: list[UserSchema], sess: Annotated[Session, Depends(get_db)]):
    return UserService.user_register(json, sess)
