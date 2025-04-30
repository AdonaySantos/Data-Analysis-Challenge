from models import users, teams, projects, logs
from database.connection import Base, engine

def create_tables():
    try:
        print("Creating tables on PostgreSQL..")
        Base.metadata.create_all(bind=engine)
        print("Tables were create")
    except Exception as e:
        print({"error": e})
