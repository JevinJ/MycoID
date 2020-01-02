from database.db_base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy_utils.types.url import URLType


class WikipediaUrl(BaseModel):
    __tablename__ = 'wikipedia_urls'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    value = Column(URLType)
