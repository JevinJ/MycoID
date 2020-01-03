from database.db_base import BaseModel
from database.mappings import Tag
from database.mixins import HasTagId
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Edibility(BaseModel):
    __tablename__ = 'edibility'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    type = relationship('EdibilityType')


class FungiEdibilityType(BaseModel, HasTagId):
    __tablename__ = 'fungi_edibility_types'
    fungi_id = Column(Integer, ForeignKey('edibility.fungi_id'), primary_key=True)


class EdibilityType(Tag):
    __mapper_args__ = {'polymorphic_identity': 'edibility'}