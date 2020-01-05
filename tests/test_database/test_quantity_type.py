from database.db_base import BaseModel, Session
from database.types import QuantityType
from hypothesis import given, settings
from hypothesis.strategies import integers, floats
from sqlalchemy import Column, Integer
from unit_registry import ureg
import pytest


class QuantityExample(BaseModel):
    id = Column(Integer, primary_key=True)
    quantity = Column(QuantityType(unit_registry=ureg))


@given(scalar_quantity=integers())
@pytest.mark.parametrize('quantity_type', [ureg.meter, ureg.millimeter, ureg.kilometer])
@settings(max_examples=5)
def test_should_insert_quantity(engine, scalar_quantity, quantity_type):
    session = Session(bind=engine)
    quantity_to_insert = scalar_quantity * quantity_type
    quantity_example = QuantityExample(quantity=quantity_to_insert)
    session.add(quantity_example)
    session.commit()
    result = session.query(QuantityExample).order_by(QuantityExample.id.desc()).first()
    assert result.quantity == quantity_to_insert


@given(scalar_quantity=floats(allow_infinity=False, allow_nan=False))
@pytest.mark.parametrize('quantity_type', [ureg.meter, ureg.millimeter, ureg.kilometer])
@settings(max_examples=5)
def test_should_insert_quantity_floats(engine, scalar_quantity, quantity_type):
    session = Session(bind=engine)
    quantity_to_insert = scalar_quantity * quantity_type
    quantity_example = QuantityExample(quantity=quantity_to_insert)
    session.add(quantity_example)
    session.commit()
    result = session.query(QuantityExample).order_by(QuantityExample.id.desc()).first()
    assert result.quantity == quantity_to_insert