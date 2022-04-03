from database import engine
from sqlalchemy import create_engine
from tables import Base

# engine = create_engine("sqlite:///./database.sqlite3")
Base.metadata.create_all(engine)
