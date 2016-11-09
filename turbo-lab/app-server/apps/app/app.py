#-*- coding:utf-8 -*-

import tornado.gen
import tornado.web

import turbo.log


from base import BaseHandler

logger = turbo.log.getLogger(__file__)


class HomeHandler(BaseHandler):

    def get(self):
        self.render('index.html')


class AsyncExceptionHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        try:
            raise ValueError()
        except Exception as e:
            response = yield tornado.gen.Task(
                self.captureException, exc_info=True
            )
        self.write('hello sentry')
        self.finish()