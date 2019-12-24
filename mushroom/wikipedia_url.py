from .base import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class WikipediaUrl(Base):
    __tablename__ = 'wikipedia_urls'
    mushroom_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    value = Column(String)