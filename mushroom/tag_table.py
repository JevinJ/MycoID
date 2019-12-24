from .base import Base
from sqlalchemy import Column, Integer, String


class TagTable(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String)
