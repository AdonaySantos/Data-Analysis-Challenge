from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from models.projects import Projects
from models.teams import Team
from schemas.user import UserSchema
from models.users import User

class UserService:
    def user_register(self, json: list[UserSchema], sess: Annotated[Session, Depends(get_db)]):
        try:
            teams_cache = {}

            for user in json:
                db_user = User(
                    id=user.id,
                    name=user.nome,
                    age=user.idade,
                    score=user.score,
                    active=user.ativo,
                    country=user.pais
                )

                team_name = user.equipe.nome
                if team_name in teams_cache:
                    db_team = teams_cache[team_name]
                else:
                    db_team = sess.query(Team).filter(Team.name == team_name).first()

                    if not db_team:
                        db_team = Team(
                            name=user.equipe.nome,
                            lider=user.equipe.lider,
                            projects=[
                                Projects(name=project.nome, completed=project.concluido) 
                                for project in user.equipe.projetos
                            ]
                        )
                        db.add(db_team)
                
                    teams_cache[team_name] = db_team  # salva no cache para próximos usuários

                db_user.team = db_team

                db_user.logs = [
                    Log(date=log.data, action=log.acao)
                    for log in user.logs
                ] if user.logs else []

                db.add(db_user)

            db.commit()
            return {"message": "Usuários inseridos com sucesso"}
        
        except Exception as e:
            db.rollback()
            return {"error": str(e)}
