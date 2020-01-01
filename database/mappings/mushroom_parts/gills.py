from ...mixins import HasReportConsensus
from database.db_base import BaseModel
from database.enums import GillAttachmentType, GillSpacingType, GillForkingType
from sqlalchemy import Column, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship


class Gills(BaseModel):
    """Description of a mushrooms' gills."""
    __tablename__ = 'gills'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    attachment = relationship('GillAttachment')
    closeness = relationship('GillSpacing')
    color = relationship('GillColor')
    forking = relationship('GillForking')
    lamellulae_tiers = relationship('GillLamellulaeTiers')


class GillForking(BaseModel, HasReportConsensus):
    __tablename__ = 'gill_forking'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)
    type = Column(Enum(GillForkingType), primary_key=True)


class GillLamellulaeTiers(BaseModel, HasReportConsensus):
    """The number of 'short gills'(Lamellulae) tiers. Lamellulae are gills
     that start at the margins of the cap but don't reach the stem. Each tier is
     a different distance to the stem. Tiers are usually 1-4, if they exist.
    """
    __tablename__ = 'gill_lamellulae_tiers'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)
    value = Column(Integer)


class GillColor(BaseModel, HasReportConsensus):
    __tablename__ = 'gill_colors'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)
    color_id = Column(Integer, ForeignKey('colors.id'), primary_key=True)


class GillAttachment(BaseModel, HasReportConsensus):
    __tablename__ = 'gill_attachment'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)
    value = Column(Enum(GillAttachmentType))


class GillSpacing(BaseModel, HasReportConsensus):
    __tablename__ = 'gill_spacing'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)
    value = Column(Enum(GillSpacingType))
