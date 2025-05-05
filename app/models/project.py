from typing import TypedDict
from pydantic import BaseModel

class ProjectDict(TypedDict):
    nome: str
    concluida: bool

class Project(BaseModel):
    nome: str
    concluida: bool
