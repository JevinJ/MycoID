from .base import Base
from .enums import EcologyType, GrowthHabit
from .tag_table import TagTable
from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship


class Ecology(Base):
    """Description of a mushrooms' habitat & ecology."""
    __tablename__ = 'ecology'
    mushroom_id = Column(Integer, ForeignKey('mushrooms.id'), primary_key=True)
    type = Column(Enum(EcologyType))
    growth_habit = Column(Enum(GrowthHabit))
    in_area_type = Column(Enum)
    associated_trees = relationship('MushroomMycorrhizalHostTag')
    on_substrates = relationship('MushroomSubstrateTag')


class EcologyTypes(Base):
    __tablename__ = 'ecology_types'
    mushroom_id = Column(Integer, ForeignKey('ecology.mushroom_id'), primary_key=True)
    ecology_type = Column(Enum(EcologyType), primary_key=True)


class MushroomMycorrhizalHostTag(Base):
    __tablename__ = 'mushroom_mycorrhizal_host_tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    mushroom_id = Column(Integer, ForeignKey('ecology.mushroom_id'))
    tag_id = Column(Integer, ForeignKey('substrate_tags.id'))


class MycorrhizalHostTag(TagTable):
    __tablename__ = 'mycorrhizal_host_tags'


class MushroomSubstrateTag(Base):
    __tablename__ = 'mushroom_substrate_tags'
    id = Column(Integer, primary_key=True)
    mushroom_id = Column(Integer, ForeignKey('ecology.mushroom_id'))
    tag_id = Column(Integer, ForeignKey('substrate_tags.id'))


class SubstrateTag(TagTable):
    """Substrates for a saprophytic mushroom."""
    __tablename__ = 'substrate_tags'





