from database.db_base import Base
from .enums import EcologyType, ClusteringHabit
from database.mixins import HasReportConsensus
from .tagging import TagTable
from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship


class Ecology(Base):
    """Description of a mushrooms' habitat & ecology."""
    __tablename__ = 'ecology'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    types = relationship('EcologyTypes')
    clustering_habit = relationship('ClusteringHabits')
    in_area_type = Column(Enum)
    mycorrhizal_hosts = relationship('FungiMycorrhizalHost')
    saprobic_substrates = relationship('FungiSaprobicSubstrate')
    parasitic_hosts = relationship('FungiParasiticHost')


class EcologyTypes(Base, HasReportConsensus):
    __tablename__ = 'ecology_types'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    ecology_type = Column(Enum(EcologyType), primary_key=True)


class ClusteringHabits(Base, HasReportConsensus):
    __tablename__ = 'clustering_habits'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    type = Column(Enum(ClusteringHabit), primary_key=True)


class FungiMycorrhizalHost(Base, HasReportConsensus):
    __tablename__ = 'fungi_mycorrhizal_hosts'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    mycorrhizal_host_id = Column(Integer, ForeignKey('mycorrhizal_hosts.id'), primary_key=True)


class FungiSaprobicSubstrate(Base, HasReportConsensus):
    __tablename__ = 'fungi_saprobic_substrates'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    saprobic_substrate_id = Column(Integer, ForeignKey('saprobic_substrates.id'), primary_key=True)


class FungiParasiticHost(Base, HasReportConsensus):
    __tablename__ = 'fungi_parasitic_hosts'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    parasitic_host_id = Column(Integer, ForeignKey('parasitic_hosts.id'), primary_key=True)


class MycorrhizalHost(Base, TagTable):
    """Organisms which a fungus grows with symbiotically."""
    __tablename__ = 'mycorrhizal_hosts'


class SaprobicSubstrate(Base, TagTable):
    """Substrates a saprophytic fungus consumes."""
    __tablename__ = 'saprobic_substrates'


class ParasiticHost(Base, TagTable):
    """Hosts which a fungus parasitizes."""
    __tablename__ = 'parasitic_hosts'
