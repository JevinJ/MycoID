from database.db_base import BaseModel
from database.mixins import HasReportConsensus
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declared_attr


class Tag(BaseModel):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    name = Column(String(64), nullable=False)
    description = Column(String)

    @declared_attr
    def __mapper_args__(self):
        if self.__name__ == 'Tag':
            return {'polymorphic_on': self.type}
        return {'polymorphic_identity': self.__name__}


class FungusTagMapping(BaseModel, HasReportConsensus):
    __abstract__ = True

    @declared_attr
    def fungus_id(self):
        return Column(Integer, ForeignKey('fungus.id'), primary_key=True)

    @declared_attr
    def tag_id(self):
        return Column(Integer, ForeignKey('tag.id'), primary_key=True)
