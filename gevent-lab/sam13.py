import gevent
from gevent import socket

def foo():
    print('Running in foo')
    gevent.sleep(0)
    #never output this
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    count = 1
    while True:
        count += 1

    print('Implicit context switch back to bar')


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])