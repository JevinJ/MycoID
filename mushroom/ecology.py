from .db_base import Base
from .enums import EcologyType, ClusteringHabit
from .tagging import TagTable, TagMapping
from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship


class Ecology(Base):
    """Description of a mushrooms' habitat & ecology."""
    __tablename__ = 'ecology'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    types = Column(Enum(EcologyType))
    clustering_habit = Column(Enum(ClusteringHabit))
    in_area_type = Column(Enum)
    mycorrhizal_hosts = relationship('FungiMycorrhizalHost')
    saprobic_substrates = relationship('FungiSaprobicSubstrate')
    parasitic_hosts = relationship('FungiParasiticHost')


class EcologyTypes(Base):
    __tablename__ = 'ecology_types'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    ecology_type = Column(Enum(EcologyType), primary_key=True)


class FungiMycorrhizalHost(TagMapping, Base):
    __tablename__ = 'fungi_mycorrhizal_hosts'


class FungiSaprobicSubstrate(TagMapping, Base):
    __tablename__ = 'fungi_saprobic_substrates'


class FungiParasiticHost(TagMapping, Base):
    __tablename__ = 'fungi_parasitic_hosts'


class MycorrhizalHost(Base, TagTable):
    """Organisms which a fungus grows with symbiotically."""
    __tablename__ = 'mycorrhizal_hosts'


class SaprobicSubstrate(Base, TagTable):
    """Substrates a saprophytic fungus consumes."""
    __tablename__ = 'saprobic_substrates'


class ParasiticHost(Base, TagTable):
    """Hosts which a fungus parasitizes."""
    __tablename__ = 'parasitic_hosts'
