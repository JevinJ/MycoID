from ..mixins import HasWidth, HasLength
from database.db_base import BaseModel
from database.mappings.color import FungusColorMapping
from database.mappings.tag import FungusTagMapping, Tag
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Spores(BaseModel):
    """Description of a mushrooms' spores."""
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    color = relationship('Color', secondary='spore_color')
    mezler_reaction = relationship('Color', secondary='fungus_mezler_reaction')
    dimensions = relationship('SporeDimensions')
    shape = relationship('SporeShape', secondary='fungus_spore_shape')
    ornamentation = relationship('SporeOrnamentation', secondary='fungus_spore_ornamentation')


class SporeDimensions(BaseModel, HasWidth, HasLength):
    id = Column(Integer, primary_key=True)
    fungus_id = Column(Integer, ForeignKey('spores.fungus_id'), primary_key=True)

SporeColor = FungusColorMapping.new_mapping('SporeColor', fungus_id_column=Spores.fungus_id)

FungusSporeShape = FungusTagMapping.new_mapping('FungusSporeShape', fungus_id_column=Spores.fungus_id)
class SporeShape(Tag): pass

FungusMezlerReaction = FungusTagMapping.new_mapping('FungusMezlerReaction', fungus_id_column=Spores.fungus_id)

FungusSporeOrnamentation = FungusTagMapping.new_mapping('FungusSporeOrnamentation', fungus_id_column=Spores.fungus_id)
class SporeOrnamentation(Tag): pass
