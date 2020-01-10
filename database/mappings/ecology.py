from database.db_base import BaseModel
from database.mappings.tag import FungusTagMapping, Tag
from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship


class Ecology(BaseModel):
    """Description of a mushrooms' habitat & ecology."""
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    types = relationship('EcologyType', secondary='fungus_ecology_type')
    clustering_habit = relationship('ClusteringHabit', secondary='fungus_clustering_habit')
    in_area_type = Column(Enum)
    mycorrhizal_hosts = relationship('MycorrhizalHost', secondary='fungus_mycorrhizal_host')
    saprobic_substrates = relationship('SaprobicSubstrate', secondary='fungus_saprobic_substrate')
    parasitic_hosts = relationship('ParasiticHost', secondary='fungus_parasitic_host')


FungusClusteringHabit = FungusTagMapping.new_mapping('FungusClusteringHabit', 'ecology.fungus_id')
class ClusteringHabit(Tag): pass

FungusEcologyType = FungusTagMapping.new_mapping('FungusEcologyType', 'ecology.fungus_id')
class EcologyType(Tag):
    """One of: mycorrhizal, parasitic, saprobic."""
    pass

FungusMycorrhizalHost = FungusTagMapping.new_mapping('FungusMycorrhizalHost', 'ecology.fungus_id')
class MycorrhizalHost(Tag):
    """Organisms which a fungus grows with symbiotically."""
    pass

FungusSaprobicSubstrate = FungusTagMapping.new_mapping('FungusSaprobicSubstrate', 'ecology.fungus_id')
class SaprobicSubstrate(Tag):
    """Substrates a saprophytic fungus consumes."""
    pass

FungusParasiticHost = FungusTagMapping.new_mapping('FungusParasiticHost', 'ecology.fungus_id')
class ParasiticHost(Tag):
    """Hosts which a fungus parasitizes."""
    pass
