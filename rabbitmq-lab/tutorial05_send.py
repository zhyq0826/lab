#!/usr/bin/python
# -*- coding: utf-8 -*-

from conn import channel, connection


# We will use a direct exchange instead. 
# The routing algorithm behind a direct exchange is simple - a message goes to the queues whose binding key exactly matches the routing key of the message.
channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')


channel.basic_publish(exchange='topic_logs',
                      routing_key='kern.error',
                      body="kern critical")


channel.basic_publish(exchange='topic_logs',
                      routing_key='kern.info',
                      body="kern info")


channel.basic_publish(exchange='topic_logs',
                      routing_key='kern.warn',
                      body="kern warn")

