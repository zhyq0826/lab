#!/usr/bin/python
# -*- coding: utf-8 -*-

from conn import channel, connection


# declare change
channel.exchange_declare(
    exchange='logs',
    exchange_type="fanout"
)


channel.basic_publish(exchange='logs',
                      routing_key='',
                      body="hello world")