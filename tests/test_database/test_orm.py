from database.mappings import *
import pytest
from sqlalchemy.ext.declarative import DeclarativeMeta
import inspect
import sys


all_orms = []
for _, obj in inspect.getmembers(sys.modules[__name__], predicate=inspect.isclass):
    if isinstance(obj, DeclarativeMeta):
        all_orms.append(obj)


@pytest.mark.parametrize('orm_class', all_orms)
def test_should_instantiate_all_orms(orm_class):
    orm_class()

