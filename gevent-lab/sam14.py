import gevent
from gevent import socket

def foo():
    print('Running in foo')
    gevent.sleep(0)
    #never output this
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    1/0

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])