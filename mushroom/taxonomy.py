from .base import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class Taxonomy(Base):
    id = Column(Integer, primary_key=True)
    mushroom_id = Column(Integer, ForeignKey('mushrooms.id'))
    common_names = Column(String)
    name_origin = Column(String)
    order = Column(String)
    family = Column(String)
    genus = Column(String)
    species = Column(String)
    variant = Column(String)
