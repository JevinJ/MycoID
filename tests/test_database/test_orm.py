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
all_fungus_tag_mapping_orms = [cls for cls in all_orms if issubclass(cls, FungusTagMapping)]


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
    @pytest.mark.parametrize('tag_type', all_tag_orms)
    def test_name_should_not_be_nullable(self, tag_type):
        assert tag_type.name.nullable is False

    def test_tag_mapper_args(self):
        assert Tag.__mapper_args__['polymorphic_on'].key == 'type'

    @pytest.mark.parametrize('tag_type', all_tag_orms)
    def test_derived_mapper_args(self, tag_type):
        if tag_type != Tag:
            assert tag_type.__mapper_args__['polymorphic_identity'] == tag_type.__name__


class TestFungusTagMapping:
    """Testing some concrete implementations of FungusTagMapping."""
    @pytest.mark.parametrize('fungus_tag_orm', all_fungus_tag_mapping_orms)
    def test_ids_should_be_foreign(self, fungus_tag_orm):
        assert len(fungus_tag_orm.fungus_id.foreign_keys) > 0
        assert len(fungus_tag_orm.tag_id.foreign_keys) > 0


class TestCap:
    pass
