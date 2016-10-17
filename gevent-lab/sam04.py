import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2
import json
import datetime

def fetch(pid):
    response = urllib2.urlopen('http://baidu.com')
    result = response.read()
    # json_result = json.loads(result)
    # datetime = json_result['datetime']

    print('Process %s: %s' % (pid, datetime))
    return result[0:10]

def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()