from database.db_base import BaseModel
from database.mappings.tag import FungusTagMapping, Tag
from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship


class Ecology(BaseModel):
    """Description of a mushrooms' habitat & ecology."""
    __tablename__ = 'ecology'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    types = relationship('EcologyType', secondary='fungus_ecology_type')
    clustering_habit = relationship('ClusteringHabit', secondary='fungus_clustering_habit')
    in_area_type = Column(Enum)
    mycorrhizal_hosts = relationship('MycorrhizalHost', secondary='fungus_mycorrhizal_host')
    saprobic_substrates = relationship('SaprobicSubstrate', secondary='fungus_saprobic_substrate')
    parasitic_hosts = relationship('ParasiticHost', secondary='fungus_parasitic_host')


class FungusEcologyType(FungusTagMapping):
    __tablename__ = 'fungus_ecology_type'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)


class FungusClusteringHabit(FungusTagMapping):
    __tablename__ = 'fungus_clustering_habit'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)


class FungusMycorrhizalHost(FungusTagMapping):
    __tablename__ = 'fungus_mycorrhizal_host'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)


class FungusSaprobicSubstrate(FungusTagMapping):
    __tablename__ = 'fungus_saprobic_substrate'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)


class FungusParasiticHost(FungusTagMapping):
    __tablename__ = 'fungus_parasitic_host'
    fungi_id = Column(Integer, ForeignKey('ecology.fungi_id'), primary_key=True)


class ClusteringHabit(Tag):
    pass


class EcologyType(Tag):
    """One of: mycorrhizal, parasitic, saprobic."""
    pass


class MycorrhizalHost(Tag):
    """Organisms which a fungus grows with symbiotically."""
    pass


class SaprobicSubstrate(Tag):
    """Substrates a saprophytic fungus consumes."""
    pass


class ParasiticHost(Tag):
    """Hosts which a fungus parasitizes."""
    pass
