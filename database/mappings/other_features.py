from database.mappings.tag import FungusTagMapping, Tag
from database.mappings.color import FungusColorMapping


class Odor(Tag): pass
class FungusOdor(FungusTagMapping): pass


class FungusLatexColor(FungusColorMapping):
    """Some mushrooms, namely lactarius, exude 'milk' or latex like
     fluid when damaged or cut."""
    pass


class BioluminescenceType(Tag): pass
class FungusBioluminescenceType(FungusTagMapping): pass


class Edibility(Tag): pass
class FungusEdibilityType(FungusTagMapping): pass


class Taste(Tag): pass
class FungusTaste(FungusTagMapping): pass


class Texture(Tag): pass