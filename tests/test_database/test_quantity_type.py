from database.db_base import BaseModel, Session
from database.column_types import QuantityType
from hypothesis import given, settings
from hypothesis.strategies import integers, floats, one_of
from sqlalchemy import Column, Integer
from unit_registry import ureg


class QuantityExample(BaseModel):
    id = Column(Integer, primary_key=True)
    quantity = Column(QuantityType(unit_registry=ureg))


@given(scalar_quantity=one_of(integers(), floats(allow_infinity=False, allow_nan=False)))
@settings(deadline=None)
def test_should_insert_quantity(engine, scalar_quantity):
    session = Session(bind=engine)
    session.query(QuantityExample).delete()
    session.commit()

    quantity_to_insert = scalar_quantity * ureg.millimeter
    quantity_example = QuantityExample(quantity=quantity_to_insert)
    session.add(quantity_example)
    session.commit()

    result = session.query(QuantityExample).first()
    assert result.quantity == quantity_to_insert
    assert result.quantity.magnitude == quantity_to_insert.magnitude
