from database.mixins import HasWidth
from database.mappings.tag import Tag, FungusTagMapping
from database.mappings.color import FungusColorMapping
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.db_base import BaseModel


class Cap(BaseModel):
    """Description of a mushrooms' cap."""
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    diameters = relationship('CapDimensions')
    colors = relationship('Color', secondary='fungus_cap_color')
    koh_reaction = relationship('Color', secondary='fungus_cap_koh_reaction')
    shape = relationship('CapShape', secondary='fungus_cap_shape')


class CapDimensions(BaseModel, HasWidth):
    id = Column(Integer, primary_key=True)
    fungus_id = Column(Integer, ForeignKey('cap.fungus_id'), primary_key=True)

FungusCapColor = FungusColorMapping.new_mapping('FungusCapColor', fungus_id_column=Cap.fungus_id)

FungusCapShape = FungusTagMapping.new_mapping('FungusCapShape', fungus_id_column=Cap.fungus_id)
class CapShape(Tag): pass

FungusCapKohReaction = FungusTagMapping.new_mapping('FungusCapKohReaction', fungus_id_column=Cap.fungus_id)
