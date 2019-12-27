from .db_base import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.hybrid import hybrid_property


class Taxonomy(Base):
    __tablename__ = 'taxonomies'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    common_names = Column(String)
    name_origin = Column(String)
    order = Column(String)
    family = Column(String)
    genus = Column(String, nullable=False)
    species = Column(String, nullable=False)
    variant = Column(String)

    @hybrid_property
    def scientific_name(self):
        return f'{self.genus} {self.species}'
