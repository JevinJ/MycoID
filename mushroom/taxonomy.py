from .base import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class Taxonomy(Base):
    __tablename__ = 'taxonomies'
    mushroom_id = Column(Integer, ForeignKey('mushrooms.id'), primary_key=True)
    common_names = Column(String)
    name_origin = Column(String)
    order = Column(String)
    family = Column(String)
    genus = Column(String, nullable=False)
    species = Column(String, nullable=False)
    variant = Column(String)
