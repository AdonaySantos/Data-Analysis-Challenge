from pydantic import BaseModel

from schemas.log import LogSchema
from schemas.team import TeamSchema

class UserSchema(BaseModel):
    id: str 
    nome: str
    idade: int
    score: int
    ativo: bool
    pais: str
    equipe: TeamSchema
    logs: list[LogSchema]
