#-*- coding: utf-8 -*-

import realpath

from datetime import datetime
import json
import time

import requests
import arrow
from sqlalchemy import inspect

from db.conn import DBSession
from models.blog import Entries, User, Tag


if __name__ == '__main__':
    class A(object):
        pass

    tag = A()
    tag.id = 90
    tag.atime = datetime.now()
    tag.name = 'tag'
    session = DBSession()
    new_tag = session.merge(tag)
    print new_tag
