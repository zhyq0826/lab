from datetime import datetime

from sqlalchemy import Column, Integer, Text , VARCHAR, BLOB, DateTime
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
    atime = Column(DateTime, default=datetime.now, nullable=False)


class Tag(Base):

    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    atime = Column(DateTime, default=datetime.now, nullable=False)



class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(255), nullable=False)
    avatar = Column(VARCHAR(255), nullable=False)
    atime = Column(DateTime, default=datetime.now, nullable=False)
    
