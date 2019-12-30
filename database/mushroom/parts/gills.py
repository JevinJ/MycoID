from ...mixins import HasReportConsensus
from database.db_base import Base
from sqlalchemy import Column, ForeignKey, String, Integer, Enum
from sqlalchemy.orm import relationship


class Gills(Base):
    """Description of a mushrooms' gills."""
    __tablename__ = 'gills'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    attachment = Column(Enum)
    closeness = Column(Enum)
    color = relationship('GillColor')
    forking = Column(String)


class GillColor(Base, HasReportConsensus):
    __tablename__ = 'gill_colors'
    fungi_id = Column(Integer, ForeignKey('gills.fungi_id'), primary_key=True)
    color_id = Column(Integer, ForeignKey('colors.id'), primary_key=True)
