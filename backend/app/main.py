from fastapi import FastAPI 
from app.api.v1 import memory, auth
from backend.app.core.database import base, engine



app = FastAPI()
base.metadata.create_all(bind=engine)  # Create the database tables




@app.get("/")
def root_route():
    return {"message": "Hello, World!"}
