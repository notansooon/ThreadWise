from sqlalchey.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
Base = declarative_base()

class MemoryModel(Base):
    __Tablename__ = 'memory_chunks'
    
    id = Column()
    
    