from database.db_base import BaseModel
from sqlalchemy import Column, Integer, String


class Tag(BaseModel):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    name = Column(String(64))
    description = Column(String)

    __mapper_args___ = {'polymorphic_on': type}