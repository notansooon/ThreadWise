import httpx
from fastapi import APIRouter, Request, Depends
from backend.app.core.database import get_db
from sqlalchemy.orm import Session
from backend.app.services.memory_service import add_memory  # Adjust the import path as necessary


NOTION_KEY = ''  # Notion API key here
DATABASE_ID = ''  # Notion database ID here

headers = {
    "authorization": f"bearer {NOTION_KEY}",
    
    

}

           

NotionRouter = APIRouter(prefix='/notion')
@NotionRouter.get("/databases")
async def getData(data: str, db: Session = Depends(get_db)):
    """
    Get all databases in the Notion workspace.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.notion.com/v1/databases/{DATABASE_ID}", headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(data)
            texts = data.get("results", [])
            print(texts)
            
            
            for data in texts:
                
                title = {
                    data["title"][0]["text"]["content"]
                    if data.get("title") else "Untitled database"
                    
                }
                payload = {
                    "memory": title,
                    "source": "notion",
                    "title": data.get("properties", {}).get("Name", {}).get("title", [{}])[0].get("text", {}).get("content", ""),
                    "time": data.get("created_time", "")
                }
                add_memory(payload, db)
        
        else:
            return {"error": "Failed to fetch databases"}