from sqlalchemy import Column, Integer, String, Text, JSON, Float, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

from app.db.base import Base

class Recipe(Base):
    __tablename__ = "recipes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    process_type = Column(String)  # smelting, fermenting, distilling, etc.
    difficulty = Column(Integer)  # skill level required (1-10)
    ingredients = Column(JSON)  # JSON of element_id:quantity pairs
    result_element_id = Column(Integer, ForeignKey("elements.id"))
    result_quantity = Column(Float)
    processing_time = Column(Integer)  # time in minutes
    tools_required = Column(ARRAY(String))  # tools needed
    temperature_required = Column(Integer, nullable=True)  # in celsius if applicable
    
    # Relationships
    result_element = relationship("Element", back_populates="recipes_as_result")
