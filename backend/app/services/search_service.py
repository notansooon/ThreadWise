from sqlalchemy.orm import Session
from app.model.memory_model import MemoryModel
from typing import List

def search(method: str, db: Session, query: str):
    if method == "semantic":
        results = search_semantic(db, query)
    else:
        results = search_keyword(db, query)
    return results

def search_keyword(db: Session, query: str) -> list[MemoryModel]:
    return db.query(MemoryModel).filter(MemoryModel.content.contains(query)).all()

def search_semantic(db: Session, query: str):
    return db.query(MemoryModel).filter(MemoryModel.content.contains(query)).all()

def search_thread(db: Session, thread_id: str):
    return db.query(MemoryModel).filter(MemoryModel.thread_id == thread_id).order_by(MemoryModel.time).all()



