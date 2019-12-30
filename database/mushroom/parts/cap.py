from ...mixins import HasWidth, HasReportConsensus
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


class CapColor(BaseModel, HasReportConsensus):
    __tablename__ = 'cap_colors'
    fungi_id = Column(Integer, ForeignKey('caps.fungi_id'), primary_key=True)
    color_id = Column(Integer, ForeignKey('colors.id'), primary_key=True)
