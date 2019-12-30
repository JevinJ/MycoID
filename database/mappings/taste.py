from database.db_base import BaseModel
from sqlalchemy import Column, Enum, Integer, ForeignKey


class Taste(BaseModel):
    __tablename__ = 'tastes'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    taste = Column(Enum)
