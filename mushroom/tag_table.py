from sqlalchemy import Column, Integer, String


class TagTable:
    id = Column(Integer, primary_key=True)
    title = Column(String)


class TagMapping:
    tag_id = Column(Integer, primary_key=True)