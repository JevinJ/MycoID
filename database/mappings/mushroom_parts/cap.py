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
    colors = relationship('CapColor')
    shape = Column(String)


class CapDimensions(BaseModel, HasWidth):
    __tablename__ = 'cap_dimensions'
    id = Column(Integer, primary_key=True)
    fungi_id = Column(Integer, ForeignKey('caps.fungi_id'), primary_key=True)


class CapColor(BaseModel, HasReportConsensus, HasColor):
    __tablename__ = 'cap_colors'
    fungi_id = Column(Integer, ForeignKey('caps.fungi_id'), primary_key=True)


class CapShape(BaseModel, HasTagId):
    fungi_id = Column(Integer, ForeignKey('caps.fungi_id'), primary_key=True)


class CapShapeType(Tag):
    __mapper_args___ = {'polymorphic_identity': 'cap_shape'}
