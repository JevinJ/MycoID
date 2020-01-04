from database.db_base import BaseModel
from database.mappings.color import FungusColorMapping
from sqlalchemy import Column, Integer, ForeignKey


class Latex(BaseModel):
    """Some mushrooms, namely lactarius, exude 'milk' or latex like
     fluid when damaged or cut."""
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)


class FungusLatexInitialColor(FungusColorMapping):
    fungus_id = Column(Integer, ForeignKey('latex.fungus_id'), primary_key=True)


class LatexOxidizedColor(FungusColorMapping):
    fungus_id = Column(Integer, ForeignKey('latex.fungus_id'), primary_key=True)


class LatexStainColor(FungusColorMapping):
    """Laxex frequently stains the flesh of a mushroom, sometimes unrelated colors."""
    fungus_id = Column(Integer, ForeignKey('latex.fungus_id'), primary_key=True)