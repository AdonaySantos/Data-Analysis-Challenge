from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import Base

class Projects(Base):
    __tablename__: str = "projects"

    id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)
    completed: Mapped[bool] = mapped_column(Boolean)

    team_id: Mapped[int] = mapped_column(Integer, ForeignKey("teams.id"))
