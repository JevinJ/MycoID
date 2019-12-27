class MycoMatch:
    pass


if __name__ == '__main__':
    from mushroom import *
    from mushroom.db_base import Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('sqlite:///mycomatch.db')
    Base.metadata.create_all(bind=engine)
    session = sessionmaker(bind=engine)()
    app = MycoMatch()
