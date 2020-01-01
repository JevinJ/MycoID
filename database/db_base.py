from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Session = sessionmaker()
BaseModel = declarative_base()
