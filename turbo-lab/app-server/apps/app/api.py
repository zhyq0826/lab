#-*- coding:utf-8 -*-

import turbo.log

from base import BaseHandler

logger = turbo.log.getLogger(__file__)


class HomeHandler(BaseHandler):

    def GET(self):
        pass

class TestCeleryHandler(BaseHandler):
    
    _get_params = {
        'option':[
            ('a', int, 0),
            ('b', int, 0),
        ]        
    }
    
    sub_task = None

    def GET(self):
        path = '/Users/zhyq0826/Documents/workspace/zhyq0826/celery-lab'
        import sys
        if path not in sys.path:
            sys.path.append(path)
        from proj import task
        task.add.delay(self._params['a'], self._params['b'])

 
