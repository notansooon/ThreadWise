from fastapi import FastAPI 
from app.api.v1 import memory, auth



app = FastAPI()




@app.get("/")
def root_route():
    return {"message": "Hello, World!"}
