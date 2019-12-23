class MycoMatch:
    pass


if __name__ == '__main__':
    from mushroom import *
    from mushroom.base import Base
    from sqlalchemy import create_engine

    engine = create_engine('sqlite:///mycomatch.db')
    Base.metadata.create_all(engine)
    app = MycoMatch()
