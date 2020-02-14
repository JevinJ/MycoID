from database.db_base import BaseModel
from database.mappings.tag import AbstractFungusTagMapping
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utils.types.color import ColorType


class Color(BaseModel):
    id = Column(Integer, primary_key=True)
    value = Column(ColorType)


class FungusColorMapping(AbstractFungusTagMapping):
    __abstract__ = True

    @declared_attr
    def tag_id(self):
        return Column(Integer, ForeignKey('color.id'), primary_key=True)
