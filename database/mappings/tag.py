from database.db_base import BaseModel
from database.mixins import HasReportConsensus
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declared_attr


class Tag(BaseModel):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    name = Column(String(64))
    description = Column(String)

    @declared_attr
    def __mapper_args__(self):
        if self.__name__ == 'Tag':
            return {'polymorphic_on': self.type}
        return {'polymorphic_identity': self.__name__}

    @staticmethod
    def new_tag_type(type_name):
        """
        :param type_name: The name of the mapper, must be identical to the variable being assigned to.
        :return: A new mapping class representing type of tag.
        """
        return type(type_name, (Tag,), {})


class FungusTagMapping(BaseModel, HasReportConsensus):
    __abstract__ = True

    @declared_attr
    def fungi_id(self):
        return Column(Integer, ForeignKey('fungi.id'), primary_key=True)

    @declared_attr
    def tag_id(self):
        return Column(Integer, ForeignKey('tag.id'), primary_key=True)

    @staticmethod
    def new_mapping(mapping_name, table_name, fungi_id_column: str):
        """
        :param mapping_name: The name of the mapper, must be identical to the variable being assigned to.
        :param table_name: The name of the table.
        :param fungi_id_column: The location of the Foreign key to use as fungi_id.
        :return: A new junction table.
        """
        return type(mapping_name, (FungusTagMapping,), {
            '__tablename__': table_name,
            'fungi_id': Column(Integer, ForeignKey(fungi_id_column), primary_key=True)
        })
