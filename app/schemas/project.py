from pydantic import BaseModel


class ProjectSchema(BaseModel):
    nome: str
    concluido: bool
