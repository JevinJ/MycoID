from database.mushroom import *
from database.db_base import Base
from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@fixture
def db_engine():
    engine = create_engine('sqlite:///:memory:')
    yield engine


@fixture
def db_session(db_engine):
    session = sessionmaker(bind=db_engine)()
    yield session
    session.close()


def test_should_create_all(db_engine):
    Base.metadata.create_all(bind=db_engine)
