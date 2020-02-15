from database.mappings import BaseModel
from database.mappings.tag import FungusTagMapping, Tag
from database.mappings.color import FungusColorMapping
from sqlalchemy import Column, ForeignKey, Integer


FungusOdor = FungusTagMapping.new_mapping('FungusOdor', fungus_id_column='fungus.id')
class Odor(Tag): pass


class FungusLatexColor(FungusColorMapping):
    """Some mushrooms, namely lactarius, exude 'milk' or latex like
     fluid when damaged or cut."""
    pass


class Bioluminescence(BaseModel):
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)


FungusEdibilityType = FungusTagMapping.new_mapping('FungusEdibilityType')
class Edibility(Tag): pass


FungusTaste = FungusTagMapping.new_mapping('FungusTaste', fungus_id_column='fungus.id')
class Taste(Tag): pass


class Texture(Tag): pass