from ..mixins import HasWidth, HasLength, HasReportConsensus
from database.db_base import BaseModel
from sqlalchemy import Column, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Spores(BaseModel):
    """Description of a mushrooms' spores."""
    __tablename__ = 'spores'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    color = relationship('SporeColor')
    mezlers_reaction = Column(Enum)
    dimensions = relationship('SporeDimensions')
    shape = Column(Enum)
    ornamentation = Column(Enum)


class SporeDimensions(BaseModel, HasWidth, HasLength):
    __tablename__ = 'spore_dimensions'
    id = Column(Integer, primary_key=True)
    fungi_id = Column(Integer, ForeignKey('spores.fungi_id'), primary_key=True)


class SporeColor(BaseModel, HasReportConsensus):
    __tablename__ = 'spore_colors'
    fungi_id = Column(Integer, ForeignKey('spores.fungi_id'), primary_key=True)
    color_id = Column(Integer, ForeignKey('colors.id'), primary_key=True)

