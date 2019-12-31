from database.mixins import HasColor, HasHeight, HasWidth
from database.db_base import BaseModel
from sqlalchemy import Column, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Stem(BaseModel):
    """Description of a mushrooms' stem."""
    __tablename__ = 'stems'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    type = Column(Enum)
    dimensions = relationship('StemDimensions')


class StemColor(BaseModel, HasColor):
    __tablename__ = 'stem_colors'
    fungi_id = Column(Integer, ForeignKey('stems.fungi_id'))


class StemDimensions(BaseModel, HasWidth, HasHeight):
    __tablename__ = 'stem_dimensions'
    id = Column(Integer, primary_key=True)
    fungi_id = Column(Integer, ForeignKey('stems.fungi_id'), primary_key=True)
