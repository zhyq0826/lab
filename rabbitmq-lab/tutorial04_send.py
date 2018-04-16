#!/usr/bin/python
# -*- coding: utf-8 -*-

from conn import channel, connection


# declare direct change
channel.exchange_declare(
    exchange='logs',
    exchange_type="fanout"
)

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')


channel.basic_publish(exchange='logs',
                      routing_key='error',
                      body="hello world")
