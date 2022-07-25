# Database Connection is here
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost/School_db"


engine=create_engine(DATABASE_URL,echo=True)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
