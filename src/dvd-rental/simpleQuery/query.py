from sqlalchemy import create_engine, Column, Integer, String
#Create a DBAPI connection
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://postres:gw@localhost:5432/scala')
# engine.dispose()
