from database.db_base import BaseModel
from database.mappings.color import FungusColorMapping
from sqlalchemy import Column, Integer, ForeignKey


class Latex(BaseModel):
    """Some mushrooms, namely lactarius, exude 'milk' or latex like
     fluid when damaged or cut."""
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)


FungusLatexInitialColor = FungusColorMapping.new_mapping('FungusLatexInitialColor', fungus_id_column=Latex.fungus_id)

FungusLatexOxidizedColor = FungusColorMapping.new_mapping('FungusLatexStainColor', fungus_id_column=Latex.fungus_id)

FungusLatexStainColor = FungusColorMapping.new_mapping('FungusLatexStainColor', fungus_id_column=Latex.fungus_id)