#-*- coding: utf-8 -*-

import gevent.monkey
gevent.monkey.patch_all()

import requests
import json

if __name__ == '__main__':
    r = requests.get('http://www.toutiao.com/api/article/pc_hot_essay/?count=4')
    entries = []
    users = []
    for i in json.loads(r.content)['data']:
        group = i['group']
        s = (group['text'][0:16], group['text'].encode('gbk'), group['digg_count'], group['comment_count'])
        entries.append(s)
        # print(s[1].encode('utf-8'))
        user = group['user']
        s = (user['user_id'], user['avatar_url'], user['name'])
        users.append(s)

    print entries
    print '========='
    print users



