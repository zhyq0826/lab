import realpath

import requests
import json
from db.conn import DBSession
from models.blog import Entries, User



def test_session_entries():
    assert isinstance(DBSession().query(Entries).all(), list)


def init_data():
    r = requests.get('http://www.toutiao.com/api/article/pc_hot_essay/?count=1000', timeout=600)
    entries = []
    users = []
    session = DBSession()
    user_set = set()
    for i in json.loads(r.content)['data']:
        group = i['group']
        user = group['user']
        e = Entries(title=group['text'][0:16], text=group['text'], dig_count=group['digg_count'], comment_count=group['comment_count'])
        e.uid = user['user_id']
        user = User(id=user['user_id'], avatar=user['avatar_url'], username=user['name'])
        if e.uid not in user_set:
            user_set.add(e.uid)
            session.add(user)
            
        session.add(e)

    session.commit()


if __name__ == '__main__':
    init_data()
