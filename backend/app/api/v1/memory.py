from fastapi import APIRouter
from app.services import memory_service
from app.services import search_service

from pydantic import baseModel

router = APIRouter()





class MemoryInput(baseModel):
    memory: str
    tags: list[str] = []
    source: str = ""
    title: str = ""
    
class MemoryOutput(baseModel):
    id: str

class queryInput(baseModel):
    query: str
    



@router.post("/ingest")
def ingest_memory(payload: MemoryInput):
    pass



@router.post("/query")
def query_memory(payload: queryInput):
    """
    Query the memory database using a search service.
    """
    query = payload.memory
    results = search_service.search(query)
    return results

@router.get("thread/{thread_id}")
def get_thread(thread_id: str):
    return memory_service.get_thread_by_id(thread_id)
    
    
    
    







 








    
    
    
             
    
    
           