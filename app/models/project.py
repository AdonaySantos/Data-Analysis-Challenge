from typing import TypedDict
from pydantic import BaseModel


class ProjectDict(TypedDict):
    nome: str
    concluido: bool


class Project(BaseModel):
    nome: str
    concluido: bool
