from pymongo.cursor import Cursor
from models.user import UserDict

def serialize_user(user: UserDict) -> UserDict:
    user['_id'] = str(user['_id'])
    return user

def list_users(users: Cursor[UserDict]) -> list[UserDict]:
    return [serialize_user(user) for user in users]
