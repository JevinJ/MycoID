from database.db_base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property


class Taxon(BaseModel):
    """Taxonomic rank, common names, or other name information about a fungus."""
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    common_names = relationship('CommonName')
    name_origin = Column(String)
    phylum = Column(String(length=64))
    class_ = Column(String(length=64))
    order = Column(String(length=64))
    family = Column(String(length=64))
    genus = Column(String(length=64), nullable=False)
    species = Column(String(length=64), nullable=False)
    variant = Column(String(length=64))

    @hybrid_property
    def scientific_name(self) -> str:
        return f'{self.genus} {self.species}'


class CommonName(BaseModel):
    id = Column(Integer, primary_key=True)
    fungus_id = Column(Integer, ForeignKey('taxon.fungus_id'), primary_key=True)
    value = Column(String(length=64), nullable=False)
