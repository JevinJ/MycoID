from database.db_base import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils.types.color import ColorType


class Color(BaseModel):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    value = Column(ColorType)
