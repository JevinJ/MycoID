from sqlalchemy import Column, Integer, Float, ForeignKey, String
from ..base import Base


class Cap(Base):
    """Description of a mushrooms' cap."""
    __tablename__ = 'caps'
    mushroom_id = Column(Integer, ForeignKey('mushrooms.id'), primary_key=True)
    min_diameter = Column(Float)
    max_diameter = Column(Float)
    color = Column(String)
    shape = Column(String)
