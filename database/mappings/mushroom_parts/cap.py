from database.mixins import HasWidth
from database.mappings.tag import Tag, FungusTagMapping
from database.mappings.chemical import ChemicalTest
from database.mappings.color import FungusColorMapping
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.db_base import BaseModel


class Cap(BaseModel):
    """Description of a mushrooms' cap."""
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    diameters = relationship('CapDimensions')
    colors = relationship('Color', secondary='fungus_cap_color')
    chemical_tests = relationship('Color', secondary='fungus_cap_chemical_test')
    shape = relationship('CapShape', secondary='fungus_cap_shape')


class CapDimensions(BaseModel, HasWidth):
    id = Column(Integer, primary_key=True)
    fungus_id = Column(Integer, ForeignKey('cap.fungus_id'), primary_key=True)

FungusCapColor = FungusColorMapping.new_mapping('FungusCapColor', fungus_id_column=Cap.fungus_id)

FungusCapShape = FungusTagMapping.new_mapping('FungusCapShape', fungus_id_column=Cap.fungus_id)
class CapShape(Tag): pass

class FungusCapChemicalTest(ChemicalTest):
    fungus_id = Column(Integer, ForeignKey('cap.fungus_id'), primary_key=True)
