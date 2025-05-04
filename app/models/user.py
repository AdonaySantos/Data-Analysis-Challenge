from typing import TypedDict
from models.log import Log
from models.team import Team

class User(TypedDict):
    id: str 
    nome: str
    idade: int
    score: int
    ativo: bool
    pais: str
    equipe: Team
    logs: list[Log]
