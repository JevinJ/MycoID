from database.db_base import BaseModel
from sqlalchemy import Column, Enum, Integer, ForeignKey


class PartialVeil(BaseModel):
    """Description of a mushrooms' partial veil."""
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    color = Column(Enum)
    type = Column(Enum)
    ring_type = Column(Enum)


class UniversalVeil(BaseModel):
    """Description of a mushrooms' universal veil(volva)."""
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    type = Column(Enum)
    remnant_type = Column(Enum)  # Remnant of a universal veil being warts, patches or powder
    remnant_color = Column(Enum)
