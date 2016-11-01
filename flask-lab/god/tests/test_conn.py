#-*- coding: utf-8 -*-

import realpath

from datetime import datetime
import json

import requests
import arrow

from db.conn import DBSession
from models.blog import Entries, User



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

if __name__ == '__main__':
    test_query_page()