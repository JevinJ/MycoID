from unit_registry import ureg
from sqlalchemy import Column, Integer
from database.column_types import QuantityType


class HasReportConsensus:
    """When a descriptive item on a fungus is tagged with a value,
     this value is incremented, when removed, decremented. This allows
     for sorting to determine the most common traits, as well as removing false traits.
     For example, if a fungus is tagged as associating with pine trees more often than oak,
     the consensus for pine would be higher."""
    report_consensus = Column(Integer, default=1)


class HasWidth:
    width = Column(QuantityType(unit_registry=ureg))


class HasHeight:
    height = Column(QuantityType(unit_registry=ureg))


class HasLength:
    length = Column(QuantityType(unit_registry=ureg))
