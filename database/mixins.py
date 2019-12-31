from unit_registry import ureg
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.hybrid import hybrid_property


class HasReportConsensus:
    """When a descriptive item on a fungus is tagged with a value,
     this value is incremented, when removed, decremented. This allows
     for sorting to determine the most common traits, as well as removing false traits.
     For example, if a fungus is tagged as associating with pine trees more often than oak,
     the consensus for pine would be higher."""
    report_consensus = Column(Integer, default=1, nullable=False)


class HasColor:
    @declared_attr
    def color_id(self):
        return Column(Integer, ForeignKey('colors.id'), primary_key=True)


class HasWidth:
    _width = Column(String(32))

    @hybrid_property
    def width(self) -> ureg.Quantity:
        return ureg.Quantity(self._width)

    @width.setter
    def width(self, value: ureg.Quantity):
        _width = str(value)


class HasHeight:
    _height = Column(String(32))

    @hybrid_property
    def height(self) -> ureg.Quantity:
        return ureg.Quantity(self._height)

    @height.setter
    def height(self, value: ureg.Quantity):
        _height = str(value)


class HasLength:
    _length = Column(String(32))

    @hybrid_property
    def length(self) -> ureg.Quantity:
        return ureg.Quantity(self._length)

    @length.setter
    def length(self, value: ureg.Quantity):
        _length = str(value)


class TagTable:
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
