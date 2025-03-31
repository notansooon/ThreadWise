from sqlalchemy import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




DATABASE_URL = ""  # Example for SQLite, change as needed
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()





