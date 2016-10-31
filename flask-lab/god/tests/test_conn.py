#-*- coding: utf-8 -*-

import realpath

import requests
import json
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


if __name__ == '__main__':
    init_data()
