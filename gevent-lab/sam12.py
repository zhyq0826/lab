import gevent
from gevent import socket

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    # this blocking call switch the control to foo
    print(socket.gethostbyname('facebook.com'))
    print('Implicit context switch back to bar')


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])