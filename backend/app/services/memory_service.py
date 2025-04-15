from app.model.memory_model import MemoryModel  # Fixed import path
from sqlalchemy.orm import Session

def get_thread_by_id(thread_id: str):
    return {
        "Thread ID": thread_id,
        "Content": []
    }

def add_memory(payload, db: Session):  # Fixed parameter name
    memory_chunk = MemoryModel(
        content=payload.memory,
        source_tool=payload.source,
        thread_id=payload.title,
        time=payload.time
    )
    db.add(memory_chunk)
    db.commit()
    db.refresh(memory_chunk)
    return {"id": memory_chunk.id}


