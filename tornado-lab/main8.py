import tornado.ioloop
import tornado.web
import tornado.gen
import logging
from concurrent.futures import ThreadPoolExecutor

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

executor = ThreadPoolExecutor(max_workers=2)

@tornado.gen.coroutine
def callback():
    """
    when a function decorator with coroutine, this function return immediately
    """
    import time
    def ca():
        print 'i am callback'
    tornado.ioloop.IOLoop.instance().add_timeout(time.time()+5, ca)


def sleep_func():
    import time
    print 'sleep start'
    time.sleep(10)
    print 'sleep end'
    return 'sleep func'

def callback2(future):
    print 'callback2'
    print future.result()


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('hello world')


class SleepHandler(tornado.web.RequestHandler):

    def get(self):
        # add one callback to ioloop, wait for next ioloop
        # this function should not be asynchronous
        tornado.ioloop.IOLoop.instance().add_callback(callback)
        self.write('sleep world')


class SleepFutureHandler(tornado.web.RequestHandler):

    #@tornado.gen.coroutine
    def get(self):
        future = executor.submit(sleep_func)
        tornado.ioloop.IOLoop.instance().add_future(future, callback2)
        self.write('sleep future')


settings = {
    'debug': True
}

application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/sleep', SleepHandler),
    (r'/sleep2', SleepFutureHandler),
],**settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()