from .db_base import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey


class Taste(Base):
    __tablename__ = 'tastes'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    taste = Column(Enum)
