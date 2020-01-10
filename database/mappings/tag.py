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

    @staticmethod
    def new_mapping(class_name, fungus_id_column: Column=None):
        """
        :param class_name: The name of the class being created, must be identical to
         the name of the variable which this is being assigned to.
        :param fungus_id_column: The column containing the fungus id of the 'left' table,
         the table being mapped to the tags.
        :return: Return a new derived class.
        """
        if fungus_id_column is None:
            return type(class_name, (FungusTagMapping,), {})
        return type(class_name, (FungusTagMapping,),
                    {'fungus_id': Column(Integer, ForeignKey(fungus_id_column), primary_key=True)})
