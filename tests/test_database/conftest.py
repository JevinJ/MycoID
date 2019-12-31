from database.db_base import BaseModel
from database.mappings import *
from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:memory:')
BaseModel.metadata.create_all(bind=engine)


@fixture(scope='module')
def db_connection():
    connection = engine.connect()
    yield connection
    connection.close()


@fixture
def db_session(db_connection):
    transaction = db_connection.begin()
    session = sessionmaker()(bind=db_connection)
    yield session
    session.close()
    transaction.rollback()
