from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@fixture
def db_engine():
    return create_engine('sqlite:///:memory:')


@fixture
def db_session(db_engine):
    session = sessionmaker(bind=db_engine)()
    yield session
    session.close()