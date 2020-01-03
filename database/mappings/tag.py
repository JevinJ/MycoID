from database.db_base import BaseModel
from sqlalchemy import Column, Integer, String
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

    @classmethod
    def new_tag_type(cls, class_name):
        return type(class_name, (cls,), {})
