from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declared_attr


class TagTable:
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)


class TagMapping:
    """Maps a fungus table to a tag table."""
    @declared_attr
    def fungus_id(self):
        return Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    tag_id = Column(Integer, primary_key=True)
    times_reported = Column(Integer, nullable=False)
