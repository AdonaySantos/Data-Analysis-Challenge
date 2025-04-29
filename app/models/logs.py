import datetime
from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import Base

class Log(Base):
    __tablename__: str = "logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime.date] = mapped_column(Date)
    action: Mapped[str] = mapped_column(String)

    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"))
