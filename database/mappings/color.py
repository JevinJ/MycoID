from database.db_base import BaseModel
from database.mixins import HasReportConsensus
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utils.types.color import ColorType


class Color(BaseModel):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    value = Column(ColorType)


class FungusColorMapping(BaseModel, HasReportConsensus):
    __abstract__ = True

    @declared_attr
    def fungi_id(self):
        return Column(Integer, ForeignKey('fungi.id'), primary_key=True)

    @declared_attr
    def color_id(self):
        return Column(Integer, ForeignKey('colors.id'), primary_key=True)
