import gevent
from gevent import socket


def create_client():
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect('./gevent-lab.sock')
    return client


if __name__ == '__main__':
    for i in range(100):
        client = create_client()
        print client.recv(2014)
        gevent.sleep(0.1)
