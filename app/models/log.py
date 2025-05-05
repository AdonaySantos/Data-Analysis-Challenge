from datetime import datetime
from typing import TypedDict
from pydantic import BaseModel

class LogDict(TypedDict):
    date: datetime
    action: str

class Log(BaseModel):
    date: datetime
    action: str
