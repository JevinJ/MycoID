from database.db_base import BaseModel
from database.mixins import HasReportConsensus
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utils.types.color import ColorType


class Color(BaseModel):
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    value = Column(ColorType)


class FungusColorMapping(BaseModel, HasReportConsensus):
    __abstract__ = True

    @declared_attr
    def fungus_id(self):
        return Column(Integer, ForeignKey('fungus.id'), primary_key=True)

    @declared_attr
    def color_id(self):
        return Column(Integer, ForeignKey('color.id'), primary_key=True)
