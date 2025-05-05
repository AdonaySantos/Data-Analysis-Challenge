from typing import TypedDict
from models.project import Project, ProjectDict
from pydantic import BaseModel

class TeamDict(TypedDict):
    nome: str
    lider: bool
    projetos: list[ProjectDict]

class Team(BaseModel):
    nome: str
    lider: bool
    projetos: list[Project]

