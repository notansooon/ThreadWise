from fastapi import APIRouter, Request, Depends
import httpx
from backend.app.core.database import get_db
from sqlalchemy.orm import Session 
from backend.app.services.memory_service import add_memory  # Adjust the import path as necessary



SlackRouter = APIRouter(prefix='/slack')



@SlackRouter.get("/channels")
def getChannel(request: Request):
    """
    Get all channels in the Slack workspace.
    """
    return {"message": "List of channels"}
    

@SlackRouter.get("/messages/{channel_id}")
async def getMessages(channel_id: str, db: Session = Depends(get_db)):
    
    SLACK_KEY = ''
        
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://slack.com/api/conversations.history?channel={channel_id}",
                            headers={"Authorization": f"Bearer "})
        if response.status_code == 200:
            data = response.json()
            message = data.get("messages", [])
        
        for messages in message:
            payload = {
                "memory": messages.get("text", ""),
                "source": "slack",
                "title": channel_id,
                "time": messages.get("ts", "")
            }
            add_memory(payload, db)
            return {"messages": message}
        else:
            return {"error": "Failed to fetch messages"}
   