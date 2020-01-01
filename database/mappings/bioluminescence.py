from database.db_base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey


class Bioluminescence(BaseModel):
    __tablename__ = 'bioluminescence'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)