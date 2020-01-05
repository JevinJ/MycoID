from sqlalchemy.types import TypeDecorator, String


class QuantityType(TypeDecorator):
    """SQLAlchemy Column type representing a pint.Quantity."""
    impl = String

    def __init__(self, unit_registry):
        super().__init__()
        self._unit_registry = unit_registry

    @property
    def python_type(self):
        return self._unit_registry.Quantity

    def process_literal_param(self, value, dialect):
        pass

    def process_bind_param(self, value, dialect):
        if value is not None and isinstance(value, self._unit_registry.Quantity):
            return str(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            return self._unit_registry.Quantity(value)
        return value

