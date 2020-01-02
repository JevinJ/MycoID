from database.db_base import BaseModel
from database.enums import EcologyType, ClusteringHabit
from database.mappings.tag import Tag
from database.mixins import HasReportConsensus
from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship


class Ecology(BaseModel):
    """Description of a mushrooms' habitat & ecology."""
    __tablename__ = 'ecology'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    types = relationship('EcologyTypes')
    clustering_habit = relationship('ClusteringHabits')
    in_area_type = Column(Enum)
    mycorrhizal_hosts = relationship('FungiMycorrhizalHost')
    saprobic_substrates = relationship('FungiSaprobicSubstrate')
    parasitic_hosts = relationship('FungiParasiticHost')


class EcologyTypes(BaseModel, HasReportConsensus):
    __tablename__ = 'ecology_types'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    ecology_type = Column(Enum(EcologyType), primary_key=True)


class ClusteringHabits(BaseModel, HasReportConsensus, HasTag):
    __tablename__ = 'clustering_habits'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    type = Column(Enum(ClusteringHabit), primary_key=True)


class FungiMycorrhizalHost(BaseModel, HasReportConsensus):
    __tablename__ = 'fungi_mycorrhizal_hosts'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    mycorrhizal_host_id = Column(Integer, ForeignKey('tag.id'), primary_key=True)


class FungiSaprobicSubstrate(BaseModel, HasReportConsensus):
    __tablename__ = 'fungi_saprobic_substrates'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    saprobic_substrate_id = Column(Integer, ForeignKey('tag.id'), primary_key=True)


class FungiParasiticHost(BaseModel, HasReportConsensus):
    __tablename__ = 'fungi_parasitic_hosts'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)
    parasitic_host_id = Column(Integer, ForeignKey('tag.id'), primary_key=True)


class EcologyType(Tag):
    """One of: mycorrhizal, parasitic, saprobic."""
    __mapper_args___ = {'polymorphic_identity': 'ecology_type'}


class MycorrhizalHost(Tag):
    """Organisms which a fungus grows with symbiotically."""
    __mapper_args___ = {'polymorphic_identity': 'mycorrhizal_host'}


class SaprobicSubstrate(Tag):
    """Substrates a saprophytic fungus consumes."""
    __mapper_args___ = {'polymorphic_identity': 'saprobic_substrate'}


class ParasiticHost(Tag):
    """Hosts which a fungus parasitizes."""
    __mapper_args___ = {'polymorphic_identity': 'parasitic_host'}
