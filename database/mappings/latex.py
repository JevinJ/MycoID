from database.db_base import BaseModel
from database.mappings.color import FungusColorMapping
from sqlalchemy import Column, Integer, ForeignKey


class Latex(BaseModel):
    """Some mushrooms, namely lactarius, exude 'milk' or latex like
     fluid when damaged or cut."""
    __tablename__ = 'latex'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)


class FungusLatexInitialColor(FungusColorMapping):
    __tablename__ = 'fungus_latex_initial_colors'
    fungi_id = Column(Integer, ForeignKey('latex.fungi_id'), primary_key=True)


class LatexOxidizedColor(FungusColorMapping):
    __tablename__ = 'fungus_latex_oxidized_colors'
    fungi_id = Column(Integer, ForeignKey('latex.fungi_id'), primary_key=True)


class LatexStainColor(FungusColorMapping):
    """Laxex frequently stains the flesh of a mushroom, sometimes unrelated colors."""
    __tablename__ = 'fungs_latex_stain_colors'
    fungi_id = Column(Integer, ForeignKey('latex.fungi_id'), primary_key=True)