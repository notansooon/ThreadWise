from fastapi import FastAPI 
from app.api.v1 import memory, auth
from backend.app.core.database import base, engine
from integration.slackAPI import SlackRouter
from integration.notionAPI import NotionRouter



app = FastAPI()
base.metadata.create_all(bind=engine)


app.include_router(memory.router, prefix="/api/v1/memory", tags=["memory"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])   

app.include_router(SlackRouter, prefix="/api/v1/slack", tags=["slack"])
app.include_router(NotionRouter, prefix="/api/v1/notion", tags=["notion"])





@app.get("/")
def root_route():
    return {"message": "Hello, World!"}
