from .db_base import Base
from .enums import EcologyType, GrowthHabit
from .tag_table import TagTable
from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship


class Ecology(Base):
    """Description of a mushrooms' habitat & ecology."""
    __tablename__ = 'ecology'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    type = Column(Enum(EcologyType))
    growth_habit = Column(Enum(GrowthHabit))
    in_area_type = Column(Enum)
    associated_trees = relationship('MushroomMycorrhizalHostTag')
    on_substrates = relationship('MushroomSubstrateTag')
    parasitic_on = relationship('MushroomParasiticHostTag')


class EcologyTypes(Base):
    __tablename__ = 'ecology_types'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    ecology_type = Column(Enum(EcologyType), primary_key=True)


class MushroomMycorrhizalHostTag(Base):
    __tablename__ = 'mushroom_mycorrhizal_host_tags'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('substrate_tags.id'), primary_key=True)


class MushroomSubstrateTag(Base):
    __tablename__ = 'mushroom_substrate_tags'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('substrate_tags.id'), primary_key=True)


class MushroomParasiticHostTag(Base):
    __tablename__ = 'mushroom_parasitic_host_tags'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('parasitic_host_tags.id'), primary_key=True)


class MycorrhizalHostTag(Base, TagTable):
    """Organisms which a fungus grows with symbiotically."""
    __tablename__ = 'mycorrhizal_host_tags'


class SubstrateTag(Base, TagTable):
    """Substrates a saprophytic fungus consumes."""
    __tablename__ = 'substrate_tags'


class ParasiticHostTag(Base, TagTable):
    """Hosts which a fungus parasitizes."""
    __tablename__ = 'parasitic_host_tags'
