#!/usr/bin/python
# -*- coding: utf-8 -*-

import pika

# connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
