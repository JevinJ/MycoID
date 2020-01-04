from database.mappings.tag import FungusTagMapping,  Tag
from sqlalchemy import Column, Integer, ForeignKey


class FungusEdibilityType(FungusTagMapping):
    __tablename__ = 'fungus_edibility_type'
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)


class Edibility(Tag):
    pass
