from typing import TypedDict
from models.project import Project

class Team(TypedDict):
    nome: str
    lider: bool
    projetcts: list[Project]

