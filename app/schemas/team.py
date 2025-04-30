from pydantic import BaseModel

from schemas.project import ProjectSchema


class TeamSchema(BaseModel):
    nome: str
    lider: bool
    projetos: list[ProjectSchema]
