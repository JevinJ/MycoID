from sqlalchemy import Column, Integer, Float, String
from ..base import Base


class Cap(Base):
    """Description of a mushrooms' cap."""
    __tablename__ = 'caps'
    id = Column(Integer, primary_key=True)
    min_diameter = Column(Float)
    max_diameter = Column(Float)
    color = Column(String)
    shape = Column(String)
