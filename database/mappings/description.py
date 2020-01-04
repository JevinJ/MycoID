from database.db_base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, String


class Description(BaseModel):
    """Basic text description for a mushroom."""
    __tablename__ = 'description'
    fungus_id = Column(Integer, ForeignKey('fungus.id'), primary_key=True)
    value = Column(String)
