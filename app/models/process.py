from sqlalchemy import Column, Integer, String, Text, JSON, ARRAY
from sqlalchemy.orm import relationship

from app.db.base import Base

class Process(Base):
    __tablename__ = "processes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    tools = Column(ARRAY(String))  # required tools
    effects = Column(JSON)  # what this process does to materials
    discovery_year = Column(Integer, nullable=True)  # historical timeline
