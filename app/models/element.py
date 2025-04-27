from sqlalchemy import Column, Integer, String, Float, Text, JSON
from sqlalchemy.orm import relationship

from app.db.base import Base

class Element(Base):
    __tablename__ = "elements"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(String)  # metal, herb, mineral, liquid, etc.
    properties = Column(JSON)  # physical/chemical properties
    rarity = Column(Float)  # how common/rare (0-10)
    description = Column(Text)
    discovery_year = Column(Integer, nullable=True)  # when discovered historically
    
    # Relationships
    recipes_as_result = relationship("Recipe", back_populates="result_element")
