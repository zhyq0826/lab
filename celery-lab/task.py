#from __future__ import absolute_import 

import time
from celery import Celery

celery = Celery('tasks', backend='rpc://', broker='redis://localhost:6379/0')

@celery.task
def sendmail(mail):
    print('send some')
    time.sleep(0.5)
    print('over')
    return 'send main %s'%mail
