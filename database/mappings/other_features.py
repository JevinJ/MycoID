from database.mappings import BaseModel
from database.mappings.tag import FungusTagMapping, Tag
from database.mappings.color import FungusColorMapping
from sqlalchemy import Column, ForeignKey, Integer


class Odor(Tag): pass
FungusOdor = FungusTagMapping.new_mapping('FungusOdor', fungus_id_column='fungus.id')


class FungusLatexColor(FungusColorMapping):
    """Some mushrooms, namely lactarius, exude 'milk' or latex like
     fluid when damaged or cut."""
    pass


class Bioluminescence(BaseModel):
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)


class Edibility(Tag): pass
FungusEdibilityType = FungusTagMapping.new_mapping('FungusEdibilityType')


class Taste(Tag): pass
FungusTaste = FungusTagMapping.new_mapping('FungusTaste', fungus_id_column='fungus.id')


class Texture(Tag): pass