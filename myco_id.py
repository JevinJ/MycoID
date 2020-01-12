class MycoID:
    pass


if __name__ == '__main__':
    from database.mappings import *
    from database.db_base import BaseModel
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('sqlite:///myco_id.db')
    BaseModel.metadata.create_all(bind=engine)
    session = sessionmaker(bind=engine)()
    app = MycoID()
