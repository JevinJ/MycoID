from database.mixins import HasHeight, HasWidth
from database.mappings.chemical import ChemicalTest
from database.mappings.color import FungusColorMapping
from database.db_base import BaseModel
from sqlalchemy import Column, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Stem(BaseModel):
    """Description of a mushrooms' stem."""
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    type = Column(Enum)
    color = relationship('Color', secondary='fungus_stem_color')
    dimensions = relationship('StemDimensions')

FungusStemColor = FungusColorMapping.new_mapping('FungusStemColor', fungus_id_column=Stem.fungus_id)

class StemDimensions(BaseModel, HasWidth, HasHeight):
    id = Column(Integer, primary_key=True)
    fungus_id = Column(Integer, ForeignKey('stem.fungus_id'), primary_key=True)

class FungusStemChemicalTest(ChemicalTest):
    fungus_id = Column(Integer, ForeignKey('stem.fungus_id'), primary_key=True)
