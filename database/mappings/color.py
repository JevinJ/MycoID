from database.db_base import BaseModel
import sqlalchemy as db
from sqlalchemy_utils.types.color import ColorType


class Color(BaseModel):
    __tablename__ = 'colors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    value = db.Column(ColorType)
