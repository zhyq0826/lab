import gevent
from gevent import socket

urls = ['baidu.com', 'googlsse.com', 'qq.com']

jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]

gevent.joinall(jobs, timeout=2)

print [job.value for job in jobs]