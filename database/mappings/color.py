from database.db_base import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utils.types.color import ColorType


class Color(BaseModel):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    value = Column(ColorType)


class FungusColorMapping(BaseModel):
    __abstract__ = True

    @declared_attr
    def fungi_id(self):
        return Column(Integer, ForeignKey('fungi.id'), primary_key=True)

    @declared_attr
    def color_id(self):
        return Column(Integer, ForeignKey('colors.id'), primary_key=True)

    @staticmethod
    def new_mapping(mapping_name, table_name, fungi_id_column: str):
        """
        :param mapping_name: The name of the mapper, must be identical to the variable being assigned to.
        :param table_name: The name of the table.
        :param fungi_id_column: The location of the Foreign key to use as fungi_id.
        :return: A new junction table.
        """
        return type(mapping_name, (FungusColorMapping,), {
            '__tablename__': table_name,
            'fungi_id': Column(Integer, ForeignKey(fungi_id_column), primary_key=True)
        })
