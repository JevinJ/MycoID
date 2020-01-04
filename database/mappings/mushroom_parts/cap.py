from database.mixins import HasWidth, HasReportConsensus, HasColor
from database.mappings.tag import Tag, FungusTagMapping
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.db_base import BaseModel


class Cap(BaseModel):
    """Description of a mushrooms' cap."""
    __tablename__ = 'caps'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    diameters = relationship('CapDimensions')
    colors = relationship('Color', secondary='cap_colors')
    shape = relationship('CapShape', secondary='fungus_cap_shape')


class CapDimensions(BaseModel, HasWidth):
    __tablename__ = 'cap_dimensions'
    id = Column(Integer, primary_key=True)
    fungi_id = Column(Integer, ForeignKey('caps.fungi_id'), primary_key=True)


class FungusCapColor(BaseModel, HasReportConsensus, HasColor):
    __tablename__ = 'cap_colors'
    fungi_id = Column(Integer, ForeignKey('caps.fungi_id'), primary_key=True)


FungusCapShape = FungusTagMapping.new_mapping('FungusCapShape', 'fungus_cap_shape', 'caps.fungi_id')
CapShape = Tag.new_tag_type('CapShape')
