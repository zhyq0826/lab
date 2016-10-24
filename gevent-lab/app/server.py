from gevent.server import StreamServer


def handle(socket, address):
    data = socket.recv(1024)
    socket.send(data)
    socket.close()


server = StreamServer(('127.0.0.1', 8000), handle)
server.serve_forever()
