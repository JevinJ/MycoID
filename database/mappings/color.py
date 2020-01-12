from database.db_base import BaseModel
from database.mixins import HasReportConsensus
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utils.types.color import ColorType


class Color(BaseModel):
    id = Column(Integer, primary_key=True)
    value = Column(ColorType)


class FungusColorMapping(BaseModel, HasReportConsensus):
    __abstract__ = True

    @declared_attr
    def fungus_id(self):
        return Column(Integer, ForeignKey('fungus.id'), primary_key=True)

    @declared_attr
    def color_id(self):
        return Column(Integer, ForeignKey('color.id'), primary_key=True)

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
            return type(class_name, (FungusColorMapping,), {})
        return type(class_name, (FungusColorMapping,),
                    {'fungus_id': Column(Integer, ForeignKey(fungus_id_column), primary_key=True)})
