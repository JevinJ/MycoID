from database.db_base import BaseModel
from sqlalchemy import Column, Enum, Integer, ForeignKey


class Smell(BaseModel):
    __tablename__ = 'smells'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    smell = Column(Enum)
