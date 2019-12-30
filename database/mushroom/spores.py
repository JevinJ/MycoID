from ..mixins import HasWidth, HasLength
from database.db_base import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Spores(Base):
    """Description of a mushrooms' spores."""
    __tablename__ = 'spores'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    color = Column(Enum)
    mezlers_reaction = Column(Enum)
    dimensions = relationship('SporeDimensions')
    shape = Column(Enum)
    ornamentation = Column(Enum)


class SporeDimensions(Base, HasWidth, HasLength):
    __tablename__ = 'spore_dimensions'
    id = Column(Integer, primary_key=True)
    fungi_id = Column(Integer, ForeignKey('spores.fungi_id'), primary_key=True)

