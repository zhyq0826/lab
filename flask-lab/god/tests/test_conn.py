#-*- coding: utf-8 -*-

import realpath

from datetime import datetime
import json
import time

import requests
import arrow

from db.conn import DBSession
from models.blog import Entries, User, Tag



def test_session_entries():
    assert isinstance(DBSession().query(Entries).all(), list)


def init_data():
    r = requests.get('http://www.toutiao.com/api/article/pc_hot_essay/?count=500', timeout=100)
    entries = []
    users = []
    session = DBSession()
    user_set = set()
    for i in session.query(User).all():
        user_set.add(i.id)

    for i in json.loads(r.content)['data']:
        group = i['group']
        user = group['user']
        # print group['text'].encode('utf-8')
        e = Entries(title=group['text'][0:16].encode('utf-8'), text=group['text'].encode('utf-8'), dig_count=group['digg_count'], comment_count=group['comment_count'])
        e.uid = user['user_id']
        user = User(id=user['user_id'], avatar=user['avatar_url'], username=user['name'].encode('utf-8'))
        if e.uid not in user_set:
            user_set.add(e.uid)
            session.add(user)
            
        session.add(e)

    session.commit()

def test_query_page():
    now = arrow.get(datetime.now())
    filter_days = [Entries.atime <  now.replace(days=1).to('local').naive, Entries.atime > now.replace(days=-1).to('local').naive]
    page_number = 1
    page_size = 100
    session = DBSession()
    while 1:
        result = session.query(Entries).filter(*filter_days).order_by(Entries.atime.desc()).offset((page_number-1)*page_size).limit(page_size).all()
        if not result:
            break
        print len(result)
        page_number += 1

def test_delete():
    session = DBSession()
    session.query(Entries).filter(Entries.id==-9).delete()


def test_flush():
    session = DBSession()
    e = session.query(Entries).filter(Entries.id == 2).first()
    print e.dig_count
    e.dig_count += -1
    session.flush()
    time.sleep(20)
    e2 = session.query(Entries).filter(Entries.id == 2).first()
    print e2.dig_count
    time.sleep(20)
    session.commit()
    session.close()

def test_session():
    import sys
    session = DBSession()
    tag = Tag(name='tag')
    session.add(tag)
    session.commit()
    tag = Tag(name='tag1')
    session.add(tag)
    session.commit()
    tag = Tag(name='tag2')
    session.add(tag)
    session.flush()
    print tag.id
    sys.stdout.flush()
    time.sleep(60)



if __name__ == '__main__':
    test_session()
