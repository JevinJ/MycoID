from .base import Base
from sqlalchemy import Column, Enum, Float, Integer, ForeignKey


class Spores(Base):
    """Description of a mushrooms' spores."""
    id = Column(Integer, primary_key=True)
    mushroom_id = Column(Integer, ForeignKey('mushrooms.id'))
    color = Column(Enum)
    mezlers_reaction = Column(Enum)
    min_length = Column(Float)
    max_length = Column(Float)
    min_width = Column(Float)
    max_width = Column(Float)
    shape = Column(Enum)
    ornamentation = Column(Enum)


