from database.db_base import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey, String


class Edibility(Base):
    __tablename__ = 'edibility'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    edibility = Column(Enum)
    notes = Column(String)
