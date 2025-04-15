from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services import memory_service, search_service
from pydantic import BaseModel  

router = APIRouter()

class MemoryInput(BaseModel):  
    memory: str
    tags: list[str] = []
    source: str = ""
    title: str = ""

class MemoryOutput(BaseModel):  
    id: str

class QueryInput(BaseModel):  
    query: str

@router.post("/ingest")
def ingest_memory(payload: MemoryInput, db: Session = Depends(get_db)):
    return memory_service.add_memory(payload)

@router.get("/search")
def search_memory(payload: QueryInput):  
    query = payload.query
    results = search_service.search(query)
    return results

@router.post("/query")
def query_memory(payload: QueryInput):  
    query = payload.query
    results = search_service.search(query)
    return results

@router.get("/thread/{thread_id}")  
def get_thread(thread_id: str):
    return memory_service.get_thread_by_id(thread_id)


























