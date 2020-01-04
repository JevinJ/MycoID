from ..mixins import HasWidth, HasLength, HasReportConsensus
from database.db_base import BaseModel
from sqlalchemy import Column, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Spores(BaseModel):
    """Description of a mushrooms' spores."""
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    color = relationship('SporeColor')
    mezlers_reaction = Column(Enum)
    dimensions = relationship('SporeDimensions')
    shape = Column(Enum)
    ornamentation = Column(Enum)


class SporeDimensions(BaseModel, HasWidth, HasLength):
    id = Column(Integer, primary_key=True)
    fungus_id = Column(Integer, ForeignKey('spores.fungus_id'), primary_key=True)


class SporeColor(BaseModel, HasReportConsensus):
    fungus_id = Column(Integer, ForeignKey('spores.fungus_id'), primary_key=True)
    color_id = Column(Integer, ForeignKey('color.id'), primary_key=True)

