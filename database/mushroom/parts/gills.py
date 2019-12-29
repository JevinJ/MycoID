from database.db_base import Base
from sqlalchemy import Column, ForeignKey, String, Integer, Enum


class Gills(Base):
    """Description of a mushrooms' gills."""
    __tablename__ = 'gills'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    attachment = Column(Enum)
    closeness = Column(Enum)
    color = Column(String)
    forking = Column(String)
