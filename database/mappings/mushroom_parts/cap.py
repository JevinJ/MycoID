from database.mixins import HasWidth, HasReportConsensus, HasTagId, HasColor
from database.mappings import Tag
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from database.db_base import BaseModel


class Cap(BaseModel):
    """Description of a mushrooms' cap."""
    __tablename__ = 'caps'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    diameters = relationship('CapDimensions')
    colors = relationship('FungiCapColor')
    shape = relationship('CapShape', )


class CapDimensions(BaseModel, HasWidth):
    __tablename__ = 'cap_dimensions'
    id = Column(Integer, primary_key=True)
    fungi_id = Column(Integer, ForeignKey('caps.fungi_id'), primary_key=True)


class FungiCapColor(BaseModel, HasReportConsensus, HasColor):
    __tablename__ = 'cap_colors'
    fungi_id = Column(Integer, ForeignKey('caps.fungi_id'), primary_key=True)


class FungusCapShape(BaseModel, HasTagId):
    __tablename__ = 'fungus_cap_shapes'
    fungi_id = Column(Integer, ForeignKey('caps.fungi_id'), primary_key=True)


class CapShape(Tag):
    pass
