from database.db_base import BaseModel, Session
from database.types import QuantityType
from hypothesis import given, settings
from hypothesis.strategies import integers
from sqlalchemy import Column, Integer
from unit_registry import ureg
import pytest


class QuantityExample(BaseModel):
    id = Column(Integer, primary_key=True)
    quantity = Column(QuantityType)


@given(scalar_quantity=integers())
@settings(max_examples=20)
def test_should_insert_quantity(engine, scalar_quantity):
    session = Session(bind=engine)
    quantity = QuantityExample(quantity=scalar_quantity * ureg.meter)
    session.add(quantity)
    session.commit()