import gevent
from gevent import Greenlet
from gevent import socket

def foo():
    print('Running in foo')
    gevent.sleep(0)
    #never output this
    print('Explicit context switch to foo again')

class Bar(Greenlet):

    def __init__(self):
        super(Bar, self).__init__() 

    def _run(self):
        print socket.gethostbyname('baidu.com')


gevent.joinall([
    gevent.spawn(foo),
])

b = Bar()
b.start()
b.join()

print('all greenlet ends')