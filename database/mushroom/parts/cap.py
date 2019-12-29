from sqlalchemy import Column, Integer, Float, ForeignKey, String
from database.db_base import Base


class Cap(Base):
    """Description of a mushrooms' cap."""
    __tablename__ = 'caps'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    min_diameter = Column(Float(precision=2))
    max_diameter = Column(Float(precision=2))
    color = Column(String(length=7))
    shape = Column(String)
