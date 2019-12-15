from ..base import Base
from sqlalchemy import Column, Integer, Float


class Stem(Base):
    """Description of a mushrooms' stem."""
    __tablename__ = 'stems'
    id = Column(Integer, primary_key=True)
    min_height = Column(Float)
    max_height = Column(Float)
    min_width = Column(Float)
    max_width = Column(Float)

