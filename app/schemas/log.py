from datetime import date
from pydantic import BaseModel


class LogSchema(BaseModel):
    data: date
    acao: str
