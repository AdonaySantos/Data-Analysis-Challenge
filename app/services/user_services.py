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


def get_team_insights() -> list[dict[str, str | int]]:
    collection = get_user_collection()
    team_insights = collection.aggregate([
        {
            "$unwind": {
                "path": "$equipe.projetos", "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$group": {
                "_id": "$equipe.nome",
                "usuarios": {"$addToSet": "$_id"},
                "lideresSet": {
                    "$addToSet": {
                        "$cond": [
                            {"$eq": ["$equipe.lider", True]},
                            "$_id",
                            None
                        ]
                    }
                },
                "projetosconcluidos": {
                    "$sum": {
                        "$cond": [
                            {"$eq": ["$equipe.projetos.concluido", True]},
                            1,
                            0
                        ]
                    }
                },
                "activeusersSet": {
                    "$addToSet": {
                        "$cond": [
                            {"$eq": ["$ativo", True]},
                            "$_id",
                            None
                        ]
                    }
                }
            }
        },
        {
            "$project": {
                "_id": 1,
                "total_users": {"$size": "$usuarios"},
                "leaders": {
                    "$size": {
                        "$filter": {
                            "input": "$lideresSet",
                            "as": "id",
                            "cond": {"$ne": ["$$id", None]}
                        }
                    }
                },
                "concluded_projects": 1,
                "active_users": {
                    "$size": {
                        "$filter": {
                            "input": "$activeusersSet",
                            "as": "id",
                            "cond": {"$ne": ["$$id", None]}
                        }
                    }
                }
            }
        }
    ])

    return percent_of_active_users(list(team_insights))


def percent_of_active_users(team_insights: list[dict[str, int | str]]):
    for team in team_insights:
        total = team["total_users"] if isinstance(
            team["total_users"], int) else 0
        active = team["active_users"] if isinstance(
            team["active_users"], int) else 0

        active_users_percent = (active * 100) / total
        team["active_users_percent"] = f"{active_users_percent:.2f}%"
    return team_insights
