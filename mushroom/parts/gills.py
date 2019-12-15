from ..base import Base
from sqlalchemy import Column, String, Integer, Enum


class Gills(Base):
    """Description of a mushrooms' gills."""
    __tablename__ = 'gills'
    id = Column(Integer, primary_key=True)
    attachment = Column(Enum)
    closeness = Column(Enum)
    color = Column(String)
    forking = Column(String)
