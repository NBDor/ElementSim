from sqlalchemy import Column, Integer, JSON, DateTime
from sqlalchemy.sql import func

from app.db.base import Base

class Inventory(Base):
    __tablename__ = "inventories"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True)  # Future: ForeignKey("users.id")
    items = Column(JSON)  # JSON of element_id:quantity pairs
    last_updated = Column(DateTime, default=func.now())
