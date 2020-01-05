from database.mappings import *
import pytest
from sqlalchemy.ext.declarative import DeclarativeMeta
import inspect
import sys


all_orms = []
for _, obj in inspect.getmembers(sys.modules[__name__], predicate=inspect.isclass):
    if isinstance(obj, DeclarativeMeta):
        all_orms.append(obj)

all_tag_orms = [cls for cls in all_orms if issubclass(cls, Tag)]


def add_and_commit(db_session, *mapped_objects):
    """Add and commit an sqlalchemy mapped object to db_session"""
    for obj in mapped_objects:
        db_session.add(obj)
    db_session.commit()


def db_session():
    from database.db_base import Session
    from tests.test_database.conftest import engine
    return Session(bind=engine)



@pytest.mark.parametrize('orm_class', all_orms)
def test_should_instantiate_all_orms(orm_class):
    orm_class()


class TestTag:
    def test_should_add_with_name(self, db_session):
        tag = Tag(name='flat')
        add_and_commit(db_session, tag)
        assert db_session.query(Tag).first().name == 'flat'

    @pytest.mark.parametrize('tag_type', all_tag_orms)
    def test_tag_name_should_be_non_nullable(self, tag_type):
        assert tag_type.name.nullable is False

    def test_should_add_with_description(self, db_session):
        tag = Tag(description='some description')
        add_and_commit(db_session, tag)
        assert db_session.query(Tag).first().description == 'some description'


class TestFungusTagMapping:
    """Testing some concrete implementations of FungusTagMapping."""
    def test_should_link_fungus_with_cap_shape(self, db_session):
        fungus = Fungus()
        cap_shape = CapShape(name='flat')
        add_and_commit(db_session, fungus, cap_shape)
        fungus_cap_shape = FungusCapShape(fungus_id=fungus.id, tag_id=cap_shape.id)
        add_and_commit(db_session, fungus_cap_shape)
        result = db_session.query(FungusCapShape).first()
        assert result.fungus_id == fungus.id and result.tag_id == cap_shape.id


class TestCap:
    pass
