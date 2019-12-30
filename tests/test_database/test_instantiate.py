from database.mushroom import *
from database.db_base import Base


def test_should_create_all(db_engine):
    Base.metadata.create_all(bind=db_engine)