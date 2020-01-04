from database.mappings.tag import FungusTagMapping,  Tag
from sqlalchemy import Column, Integer, ForeignKey


class FungusEdibilityType(FungusTagMapping):
    __tablename__ = 'fungus_edibility_type'


class Edibility(Tag):
    pass
