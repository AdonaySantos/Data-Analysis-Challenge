from typing import TypedDict
from models.log import Log, LogDict
from models.team import Team, TeamDict
from pydantic import BaseModel, Field


# TypedDict to type data that will be used in MongoDB
class UserDict(TypedDict):
    _id: str
    nome: str
    idade: int
    score: int
    ativo: bool
    pais: str
    equipe: TeamDict
    logs: list[LogDict]


# pydantic BaseModel to add validations
class User(BaseModel):
    id: str = Field(validation_alias="id", alias="_id")
    nome: str
    idade: int
    score: int
    ativo: bool
    pais: str
    equipe: Team
    logs: list[Log]
