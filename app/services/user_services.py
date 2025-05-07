from pymongo.cursor import Cursor
from database.mongo import get_user_collection
from models.user import UserDict


def get_all_superusers():
    collection = get_user_collection()
    superusers: list[Cursor[UserDict]] = list(collection.find({
        "score": {"$gte": 900}, "ativo": True
    }))
    if not superusers:
        return "Superusers not found"
    return superusers


def get_all_top_countries():
    collection = get_user_collection()
    top_countries = collection.aggregate([
        {
            "$match": {
                "score": {"$gte": 900},
                "ativo": True
            }
        },
        {
            "$group": {
                "_id": "$pais",
                "totalSuperUsuarios": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "totalSuperUsuarios": -1
            }
        },
        {
            "$limit": 5
        }
    ])

    return list(top_countries)
