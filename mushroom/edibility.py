from .base import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey, String


class Edibility(Base):
    __tablename__ = 'edibility'
    id = Column(Integer, primary_key=True)
    mushroom_id = Column(Integer, ForeignKey('mushrooms.id'))
    edibility = Column(Enum)
    notes = Column(String)
