from .db_base import Base
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship


class Fungus(Base):
    """Information/data in common with all fungi."""
    __tablename__ = 'fungi'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = relationship('Description', uselist=False, backref='fungus')
    ecology = relationship('Ecology', uselist=False, backref='fungus')
    smell = relationship('Smell', uselist=False, backref='fungus')
    spores = relationship('Spores', uselist=False, backref='fungus')
    taste = relationship('Taste', uselist=False, backref='fungus')
    taxonomy = relationship('Taxon', uselist=False, backref='fungus')
    wikipedia_url = relationship('WikipediaUrl', uselist=False, backref='fungus')


