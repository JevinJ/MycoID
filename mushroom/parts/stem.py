from ..db_base import Base
from sqlalchemy import Column, Enum, Integer, Float, ForeignKey


class Stem(Base):
    """Description of a mushrooms' stem."""
    __tablename__ = 'stems'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    type = Column(Enum)
    min_height = Column(Float)
    max_height = Column(Float)
    min_width = Column(Float)
    max_width = Column(Float)

