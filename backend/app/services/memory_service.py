

from backend.model.memoru_model import MemoryModel
from sqlalchemy.orm import Session

def get_thread_by_id(thread_id: str):
    return {
        "Thread ID": thread_id, 
        "Content": []
    }


def add_memory(payload, bd: Session ):
    memory_chunk = MemoryModel(
        payload.content,
    )
        
    
