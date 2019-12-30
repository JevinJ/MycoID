from database.db_base import BaseModel
from sqlalchemy import Column, Enum, Integer, ForeignKey, String


class Edibility(BaseModel):
    __tablename__ = 'edibility'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    edibility = Column(Enum)
    notes = Column(String)
