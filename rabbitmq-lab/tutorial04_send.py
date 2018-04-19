#!/usr/bin/python
# -*- coding: utf-8 -*-

from conn import channel, connection


# We will use a direct exchange instead. 
# The routing algorithm behind a direct exchange is simple - a message goes to the queues whose binding key exactly matches the routing key of the message.
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')


channel.basic_publish(exchange='direct_logs',
                      routing_key='error',
                      body="hello world")
