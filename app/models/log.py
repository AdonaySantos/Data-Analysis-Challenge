from datetime import datetime
from typing import TypedDict

class Log(TypedDict):
    date: datetime
    action: str
