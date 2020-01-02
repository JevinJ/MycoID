from database.mappings import Tag
from database.mixins import HasReportConsensus, HasTag, HasColor
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


class GillForking(BaseModel, HasReportConsensus, HasTag):
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


class GillAttachment(BaseModel, HasReportConsensus, HasTag):
    __tablename__ = 'gill_attachment'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)


class GillSpacing(BaseModel, HasReportConsensus, HasTag):
    __tablename__ = 'gill_spacing'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)


class GillEdge(BaseModel, HasReportConsensus, HasTag):
    __tablename__ = 'gill_edge'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)


class GillForkingType(Tag):
    __mapper_args___ = {'polymorphic_identity': 'gill_forking_type'}


class HymeniumAttachmentType(Tag):
    __mapper_args___ = {'polymorphic_identity': 'hymenium_attachment_type'}


class GillSpacingType(Tag):
    __mapper_args___ = {'polymorphic_identity': 'gill_spacing_type'}


class GillEdgeType(Tag):
    __mapper_args___ = {'polymorphic_identity': 'gill_edge_type'}
