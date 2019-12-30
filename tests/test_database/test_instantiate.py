from database.mappings import *
from database.db_base import BaseModel
import pytest
from sqlalchemy.ext.declarative import DeclarativeMeta
import inspect
import sys


def test_should_create_all(db_engine):
    BaseModel.metadata.create_all(bind=db_engine)


all_orms = []
for _, obj in inspect.getmembers(sys.modules[__name__], predicate=inspect.isclass):
    if isinstance(obj, DeclarativeMeta):
        all_orms.append(obj)


@pytest.mark.parametrize('orm_class', all_orms)
def test_should_instantiate_all_orms(orm_class):
    orm_class()

