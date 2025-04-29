from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.connection import Base
from models.projects import Projects

class Team(Base):
    __tablename__: str = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    lider: Mapped[bool] = mapped_column(Boolean)

    projects: Mapped[list["Projects"]] = relationship("Project", backref="team")
    
