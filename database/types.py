from unit_registry import ureg
from sqlalchemy.types import TypeDecorator, String


class QuantityType(TypeDecorator):
    """SQLAlchemy Column type representing a pint.Quantity."""
    impl = String
    python_type = ureg.Quantity

    def process_literal_param(self, value, dialect):
        pass

    def process_bind_param(self, value, dialect):
        if value is not None and isinstance(value, ureg.Quantity):
            return str(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            return ureg.Quantity(value)
        return value

