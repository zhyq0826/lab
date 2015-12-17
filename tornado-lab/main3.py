from tornado import httpserver
from tornado import ioloop
 
def handle_request(request):
    message = "You requested %s\n" % request.uri
    request.write("HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s" % (
                 len(message), message))
    request.finish()
 

# server = httpserver.HTTPServer(app)
# server.listen(8888)
# ioloop.IOLoop.current().start()

# sockets = tornado.netutil.bind_sockets(8888)
# tornado.process.fork_processes(0)
# server = HTTPServer(app)
# server.add_sockets(sockets)
# IOLoop.current().start()

http_server = httpserver.HTTPServer(handle_request)
http_server.bind(8888)
http_server.start()
ioloop.IOLoop.instance().start()