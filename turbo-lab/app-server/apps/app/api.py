#-*- coding:utf-8 -*-

import os
import sys
import turbo.log
from turbo import app_config


from base import BaseHandler

logger = turbo.log.getLogger(__file__)

task_path = os.path.join(os.path.dirname(app_config.app_setting.project_dir), 'celery-lab')
sys.path.append(task_path)

from proj import task

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
        task.add.delay(self._params['a'], self._params['b'])

 
