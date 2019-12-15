from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Mushroom(Base):
    """Information/data in common with all mushrooms."""
    __tablename__ = 'mushrooms'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    habitat = relationship('Habitat', uselist=False, backref='mushrooms')
    smell = relationship('Smell', uselist=False, backref='mushrooms')
    spores = relationship('Spore', uselist=False, backref='mushrooms')
    taste = relationship('Taste', uselist=False, backref='mushrooms')
    taxonomy = relationship('Taxonomy', uselist=False, backref='mushrooms')
    wikipedia_url = Column(String)
