# -*- encoding: utf-8 -*-
#ioloop.py 主要的是将底层的epoll或者说是其他的IO多路复用封装作异步事件来处理。
# 可以看到在注释前都是使用了传统的创建服务器的方式，不用多介绍，注意就是把套接口设置为非阻塞方式。
# 创建ioloop实例，这里是使用了ioloop.IOLoop中的 instance()静态方法，以 @classmethod 方式包装。
# 在后面的add_handler中，程序为我们的监听套接口注册了一个回调函数和一个事件类型。
# 在注册了相应的事件类型和回调函数以后，程序开始启动，如果在相应的套接口上有事件发生（注册的事件类型）那么调用相应的回调函数。
# 当监听套接口有可读事件发生，意味着来了一个新连接，在回调函数中就可以对这个套接口accept，并调用相应的处理函数，其实应该是处理函数也设置为异步的，将相应的连接套接口也加入到事件循环并注册相应的回调函数，只是这里没有展示出来。
# 在使用非阻塞方式的accept时候常常返回EAGAIN,EWOULDBLOCK 错误，这里采取的方式是放弃这个连接。


# normal
# while true {
#     for i in stream[]; {
#         if i has data
#             read until unavailable
#     }
# }

# select
# while true {
#     select(streams[])
#     for i in streams[] {
#         if i has data
#             read until unavailable
#     }
# }


# epoll
# while true {
#     active_stream[] = epoll_wait(epollfd)
#     for i in active_stream[] {
#         read or write till unavailable
#     }
# }



import errno
import functools
import tornado.ioloop
import socket
import time

def handle_connection(connection, address):
    print connection
    print address

def connection_ready(sock, fd, events):
    while True:
        try:
            connection, address = sock.accept()
        except socket.error as e:
            if e.args[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
                raise
            return
        connection.setblocking(0)
        handle_connection(connection, address)

if __name__ == '__main__':
    port = 8888
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(0)
    sock.bind(("", port))
    sock.listen(128)

    io_loop = tornado.ioloop.IOLoop.current()
    callback = functools.partial(connection_ready, sock)
    io_loop.add_handler(sock.fileno(), callback, io_loop.READ)
    io_loop.start()