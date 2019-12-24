from sqlalchemy import Column, Integer, String


class TagTable:
    id = Column(Integer, primary_key=True)
    title = Column(String)
