from database.mappings import BaseModel
from database.mappings.tag import Tag
from database.mixins import HasReportConsensus
from sqlalchemy import Column, Integer, ForeignKey


class ChemicalTestType(Tag): pass
class ChemicalTest(BaseModel, HasReportConsensus):
    """Maps a fungus to a type of chemical test(like KOH) and the resulting color of that test.
     This is abstract because the result of a test can depend on which part of a fungus it is
     applied to, so different parts need their own tables."""
    __abstract__ = True

    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    color_id = Column(Integer, ForeignKey('color.id'), primary_key=True)
    type = Column(Integer, ForeignKey('tag.id'), primary_key=True)