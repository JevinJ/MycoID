from .base import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey


class Taste(Base):
    __tablename__ = 'tastes'
    mushroom_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    taste = Column(Enum)
