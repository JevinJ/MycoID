from database.db_base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, String


class Description(BaseModel):
    """Basic text description for a mushroom."""
    __tablename__ = 'descriptions'
    fungi_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    value = Column(String)
