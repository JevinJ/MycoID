from database.mappings.color import FungusColorMapping
from database.mappings.tag import FungusTagMapping, Tag
from database.db_base import BaseModel
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Gills(BaseModel):
    """Description of a mushrooms' gills."""
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    attachment = relationship('HymeniumAttachment', secondary='fungus_hymenium_attachment')
    closeness = relationship('GillSpacing', secondary='fungus_gill_spacing')
    color = relationship('Color', secondary='fungus_gill_color')
    edge = relationship('GillEdge', secondary='fungus_gill_edge')
    forking = relationship('GillForking', secondary='fungus_gill_forking')
    lamellulae_tiers = relationship('GillLamellulaeTiers')
    texture = relationship('Texture', secondary='fungus_gill_texture')


class GillLamellulaeTiers(BaseModel):
    """The number of 'short gills'(Lamellulae) tiers. Lamellulae are gills
     that start at the margins of the cap but don't reach the stem. Each tier is
     a different distance to the stem. Tiers are usually 1-4, if they exist.
    """
    fungus_id = Column(Integer, ForeignKey('gills.fungus_id'), primary_key=True)
    value = Column(Integer)


FungusGillColor = FungusColorMapping.new_mapping('FungusGillColor', fungus_id_column=Gills.fungus_id)


FungusGillForking = FungusTagMapping.new_mapping('FungusGillForking', fungus_id_column=Gills.fungus_id)
class GillForking(Tag): pass

FungusHymeniumAttachment = FungusTagMapping.new_mapping('FungusHymeniumAttachment', fungus_id_column=Gills.fungus_id)
class HymeniumAttachment(Tag): pass

FungusGillSpacing = FungusTagMapping.new_mapping('FungusGillSpacing', fungus_id_column=Gills.fungus_id)
class GillSpacing(Tag): pass

FungusGillEdge = FungusTagMapping.new_mapping('FungusGillEdge', fungus_id_column=Gills.fungus_id)
class GillEdge(Tag): pass

FungusGillTexture = FungusTagMapping.new_mapping('FungusGillTexture', fungus_id_column=Gills.fungus_id)
