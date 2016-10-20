from sqlalchemy import Column, Integer, Text , VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Entries(Base):

    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    text = Column(Text, nullable=False)


class Tag(Base):

    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)

