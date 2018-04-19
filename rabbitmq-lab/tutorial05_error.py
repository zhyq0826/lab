#!/usr/bin/python
# -*- coding: utf-8 -*-

from conn import channel, connection


channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')


# random queue result.method.queue
# Secondly, once the consumer connection is closed, 
# the queue should be deleted. There's an exclusive flag for that:
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# routing key specify the queue consume certain message
channel.queue_bind(exchange='topic_logs',
                   queue=queue_name,
                   routing_key='*.error'
               )

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
