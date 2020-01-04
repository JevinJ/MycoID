from database.mappings.tag import FungusTagMapping,  Tag
from sqlalchemy import Column, Integer, ForeignKey


class FungusEdibilityType(FungusTagMapping):
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)


class Edibility(Tag):
    pass
