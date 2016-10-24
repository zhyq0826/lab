from sqlalchemy import Column, Integer, Text , VARCHAR, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Entries(Base):

    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(BLOB, nullable=False)
    text = Column(BLOB, nullable=False)
    dig_count = Column(Integer)
    uid = Column(Integer)
    comment_count = Column(Integer)


class Tag(Base):

    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)


class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR, nullable=False)
    avatar = Column(VARCHAR, nullable=False)