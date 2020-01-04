import inflection
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()


@as_declarative()
class BaseModel:
    @declared_attr
    def __tablename__(self):
        return inflection.underscore(self.__name__)
