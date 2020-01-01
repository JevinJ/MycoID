from database.db_base import BaseModel
from database.mixins import HasColor, HasReportConsensus
from sqlalchemy import Column, Integer, ForeignKey


class Latex(BaseModel):
    """Some mushrooms, namely lactarius, exude 'milk' or latex like
     fluid when damaged or cut."""
    __tablename__ = 'latex'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)


class LatexInitialColor(BaseModel, HasColor, HasReportConsensus):
    __tablename__ = 'latex_initial_colors'
    fungi_id = Column(Integer, ForeignKey('latex.fungi_id'), primary_key=True)


class LatexOxidizedColor(BaseModel, HasColor, HasReportConsensus):
    __tablename__ = 'latex_oxidized_colors'
    fungi_id = Column(Integer, ForeignKey('latex.fungi_id'), primary_key=True)


class LatexStainColor(BaseModel, HasColor, HasReportConsensus):
    """Laxex frequently stains the flesh of a mushroom, sometimes unrelated colors."""
    __tablename__ = 'latex_stain_colors'
    fungi_id = Column(Integer, ForeignKey('latex.fungi_id'), primary_key=True)