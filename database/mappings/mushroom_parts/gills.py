from ...mixins import HasReportConsensus
from database.db_base import BaseModel
from database.enums import GillAttachmentType, GillSpacingType
from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Enum
from sqlalchemy.orm import relationship


class Gills(BaseModel):
    """Description of a mushrooms' gills."""
    __tablename__ = 'gills'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    attachment = relationship('GillAttachment')
    closeness = relationship('GillSpacing')
    color = relationship('GillColor')
    forking = Column(String)
    has_lamellulae = relationship('GillLamellulae')


class GillLamellulae(BaseModel, HasReportConsensus):
    """Describes if mushroom's gills have 'short gills'(Lamellulae)"""
    __tablename__ = 'gill_lamellulae'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)
    value = Column(Boolean)


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
