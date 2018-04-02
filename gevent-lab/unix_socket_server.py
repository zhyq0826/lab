import os
import random

from gevent.baseserver import BaseServer
from gevent import socket, sleep


def _unix_socket_listener(pathname, backlog=50):
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sockname = pathname + '.sock'
    if os.path.exists(sockname):
        os.remove(sockname)
    try:
        sock.bind(sockname)
    except socket.error as ex:
        strerror = getattr(ex, 'strerror', None)
        if strerror is not None:
            ex.strerror = strerror + ': ' + sockname
        raise
    sock.listen(backlog)
    sock.setblocking(0)
    return sock


class UnixSocketTCPServer(BaseServer):
    backlog = 256

    def __init__(self, pathname, handle=None, backlog=None):
        try:
            if backlog is not None:
                if hasattr(self, 'socket'):
                    raise TypeError('backlog must be None when a socket instance is passed')
                self.backlog = backlog
        except:
            self.close()
            raise

        listener = _unix_socket_listener(pathname, self.backlog)
        super(UnixSocketTCPServer, self).__init__(listener, handle)

    def do_close(self, sock, *args):
        sock.close()

    def do_read(self):
        try:
            client_socket, address = self.socket.accept()
        except socket.error as err:
            if err.args[0] == socket.EWOULDBLOCK:
                return
            raise
        sockobj = socket.socket(_sock=client_socket)
        return sockobj, address


def handle(sockobj, address):
    print sockobj, address
    sockobj.sendall("hello")
    sleep(random.choice([1, 2, 3]))


if __name__ == '__main__':
    server = UnixSocketTCPServer('./gevent-lab', handle=handle)
    server.serve_forever()
