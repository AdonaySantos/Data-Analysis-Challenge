from datetime import datetime
from typing import TypedDict
from pydantic import BaseModel


class LogDict(TypedDict):
    data: datetime
    acao: str


class Log(BaseModel):
    data: datetime
    acao: str
