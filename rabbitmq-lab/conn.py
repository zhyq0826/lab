#!/usr/bin/python
# -*- coding: utf-8 -*-

import pika

# connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# declare queue 
# If we send a message to non-existing location, RabbitMQ will just drop the message
channel.queue_declare(queue='hello')