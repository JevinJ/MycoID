from database.mixins import HasHeight, HasWidth
from database.mappings.color import FungusColorMapping
from database.db_base import BaseModel
from sqlalchemy import Column, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Stem(BaseModel):
    """Description of a mushrooms' stem."""
    __tablename__ = 'stem'
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    type = Column(Enum)
    dimensions = relationship('StemDimensions')


class StemColor(FungusColorMapping):
    __tablename__ = 'stem_color'
    fungus_id = Column(Integer, ForeignKey('stem.fungus_id'))


class StemDimensions(BaseModel, HasWidth, HasHeight):
    __tablename__ = 'stem_dimensions'
    id = Column(Integer, primary_key=True)
    fungus_id = Column(Integer, ForeignKey('stem.fungus_id'), primary_key=True)
