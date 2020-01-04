from database.db_base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey


class Bioluminescence(BaseModel):
    __tablename__ = 'bioluminescence'
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)