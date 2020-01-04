from database.db_base import BaseModel
from sqlalchemy import Column, Enum, Integer, ForeignKey


class Smell(BaseModel):
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    smell = Column(Enum)
