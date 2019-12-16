from ..base import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey


class PartialVeil(Base):
    """Description of a mushrooms' partial veil."""
    id = Column(Integer, primary_key=True)
    mushroom_id = Column(Integer, ForeignKey('mushrooms.id'))
    color = Column(Enum)
    type = Column(Enum)


class UniversalVeil(Base):
    """Description of a mushrooms' universal veil(volva)."""
    id = Column(Integer, primary_key=True)
    mushroom_id = Column(Integer, ForeignKey('mushrooms.id'))
    type = Column(Enum)
    remnant_type = Column(Enum)  # Remnant of a universal veil being warts, patches or powder
    remnant_color = Column(Enum)
