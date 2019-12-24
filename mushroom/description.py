from .base import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class Description(Base):
    """Basic text description for a mushroom."""
    __tablename__ = 'descriptions'
    mushroom_id = Column(Integer, ForeignKey('fungi.id'), primary_key=True)
    value = Column(String)
