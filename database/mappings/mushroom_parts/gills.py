from database.mappings import Tag
from database.mixins import HasReportConsensus, HasTagId, HasColor
from database.db_base import BaseModel
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Gills(BaseModel):
    """Description of a mushrooms' gills."""
    __tablename__ = 'gills'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    attachment = relationship('GillAttachment')
    closeness = relationship('GillSpacing')
    color = relationship('GillColor')
    edge = relationship('GillEdge')
    forking = relationship('GillForking')
    lamellulae_tiers = relationship('GillLamellulaeTiers')
    texture = relationship('GillTexture')


class GillForking(BaseModel, HasReportConsensus, HasTagId):
    __tablename__ = 'gill_forking'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)


class GillLamellulaeTiers(BaseModel):
    """The number of 'short gills'(Lamellulae) tiers. Lamellulae are gills
     that start at the margins of the cap but don't reach the stem. Each tier is
     a different distance to the stem. Tiers are usually 1-4, if they exist.
    """
    __tablename__ = 'gill_lamellulae_tiers'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)
    value = Column(Integer)


class GillColor(BaseModel, HasReportConsensus, HasColor):
    __tablename__ = 'gill_colors'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)


class GillAttachment(BaseModel, HasReportConsensus, HasTagId):
    __tablename__ = 'gill_attachment'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)


class GillSpacing(BaseModel, HasReportConsensus, HasTagId):
    __tablename__ = 'gill_spacing'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)


class GillEdge(BaseModel, HasReportConsensus, HasTagId):
    __tablename__ = 'gill_edge'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)


class GillTexture(BaseModel, HasReportConsensus, HasTagId):
    __tablename__ = 'gill_texture'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)


GillForkingType = Tag.new_tag_type('GillForkingType')
HymeniumAttachmentType = Tag.new_tag_type('HymeniumAttachmentType')
GillSpacingType = Tag.new_tag_type('GillSpacingType')
GillEdgeType = Tag.new_tag_type('GillEdgeType')
