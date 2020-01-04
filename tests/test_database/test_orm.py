from database.mappings import *
import pytest
from sqlalchemy.ext.declarative import DeclarativeMeta
import inspect
import sys


all_orms = []
for _, obj in inspect.getmembers(sys.modules[__name__], predicate=inspect.isclass):
    if isinstance(obj, DeclarativeMeta):
        all_orms.append(obj)


def add_and_commit(db_session, mapped_object):
    """Add and commit an sqlalchemy mapped object to db_session"""
    db_session.add(mapped_object)
    db_session.commit()


@pytest.mark.parametrize('orm_class', all_orms)
def test_should_instantiate_all_orms(orm_class):
    orm_class()


class TestTag:
    def test_should_add_with_name(self, db_session):
        tag = Tag(name='flat')
        db_session.add(tag)
        db_session.commit()
        assert db_session.query(Tag).first().name == 'flat'

    def test_should_add_with_description(self, db_session):
        tag = Tag(description='some description')
        db_session.add(tag)
        db_session.commit()
        assert db_session.query(Tag).first().description == 'some description'
