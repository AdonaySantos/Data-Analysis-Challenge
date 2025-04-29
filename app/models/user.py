from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.connection import Base
from models.teams import Team
from .logs import Log

class User(Base):
    __tablename__: str = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True)

    name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    score: Mapped[int] = mapped_column(Integer)
    active: Mapped[bool] = mapped_column(Boolean)
    country: Mapped[str] = mapped_column(String)

    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    team: Mapped["Team"] = relationship("Team", backref="user")

    logs: Mapped[list["Log"]] = relationship("Log", backref="user", cascade="all, delete-orphan")

