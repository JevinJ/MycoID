from database.mixins import HasWidth
from database.mappings.tag import Tag, FungusTagMapping
from database.mappings.color import FungusColorMapping
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.db_base import BaseModel


class Cap(BaseModel):
    """Description of a mushrooms' cap."""
    __tablename__ = 'caps'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    diameters = relationship('CapDimensions')
    colors = relationship('Color', secondary='fungus_cap_color')
    shape = relationship('CapShape', secondary='fungus_cap_shape')


class CapDimensions(BaseModel, HasWidth):
    __tablename__ = 'cap_dimensions'
    id = Column(Integer, primary_key=True)
    fungi_id = Column(Integer, ForeignKey('caps.fungi_id'), primary_key=True)


class FungusCapColor(FungusColorMapping):
    __tablename__ = 'fungus_cap_color'
    fungi_id = Column(Integer, ForeignKey('caps.fungi_id'), primary_key=True)


class FungusCapShape(FungusTagMapping):
    __tablename__ = 'fungus_cap_shape'
    fungi_id = Column(Integer, ForeignKey('caps.fungi_id'), primary_key=True)


class CapShape(Tag): pass
