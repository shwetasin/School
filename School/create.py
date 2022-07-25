# from database import Base, engine
from app.config.dbconfig import Base,engine
# from models import *
from app.config.model import *
print("Creating database ....")

Base.metadata.create_all(engine)

print("Created database ....")