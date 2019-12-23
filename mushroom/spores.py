from .base import Base
from sqlalchemy import Column, Enum, Float, Integer, ForeignKey


class Spores(Base):
    """Description of a mushrooms' spores."""
    __tablename__ = 'spores'
    mushroom_id = Column(Integer, ForeignKey('mushrooms.id'), primary_key=True)
    color = Column(Enum)
    mezlers_reaction = Column(Enum)
    min_length = Column(Float)
    max_length = Column(Float)
    min_width = Column(Float)
    max_width = Column(Float)
    shape = Column(Enum)
    ornamentation = Column(Enum)


