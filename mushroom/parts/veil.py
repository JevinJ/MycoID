from ..db_base import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey


class PartialVeil(Base):
    """Description of a mushrooms' partial veil."""
    __tablename__ = 'partial_veils'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    color = Column(Enum)
    type = Column(Enum)
    ring_type = Column(Enum)


class UniversalVeil(Base):
    """Description of a mushrooms' universal veil(volva)."""
    __tablename__ = 'universal_veils'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    type = Column(Enum)
    remnant_type = Column(Enum)  # Remnant of a universal veil being warts, patches or powder
    remnant_color = Column(Enum)
