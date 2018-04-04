#!/usr/bin/python
# -*- coding: utf-8 -*-

from conn import channel, connection

# In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchang
# All we need to know now is how to use a default exchange identified by an empty string. This exchange is special ‒ it allows us to specify exactly to which queue the message should go. The queue name needs to be specified in the routing_key parameter:
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
