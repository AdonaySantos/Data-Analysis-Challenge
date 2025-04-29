from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from core.config_dotenv import DATABASE_URL

engine = create_engine(DATABASE_URL)

Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

def get_db():
    sess = Session()
    try:
        yield sess
    finally:
        sess.close()
