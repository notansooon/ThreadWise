from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class MemoryModel(Base):
    __tablename__ = 'memory_chunks'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(Text, nullable=False)
    source_tool = Column(String, nullable=False)
    thread_id = Column(String, nullable=False)
    time = Column(DateTime, nullable=False)
    
