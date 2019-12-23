from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Mushroom(Base):
    """Information/data in common with all mushrooms."""
    __tablename__ = 'mushrooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    ecology = relationship('Ecology', uselist=False, backref='mushroom')
    smell = relationship('Smell', uselist=False, backref='mushroom')
    spores = relationship('Spores', uselist=False, backref='mushroom')
    taste = relationship('Taste', uselist=False, backref='mushroom')
    taxonomy = relationship('Taxonomy', uselist=False, backref='mushroom')
    wikipedia_url = Column(String)
