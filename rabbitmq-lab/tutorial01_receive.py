# -*- coding: utf-8 -*-

from conn import channel

# Creating a queue using queue_declare is idempotent
# ‒ we can run the command as many times as we like, and only one will be created.
# sudo rabbitmqctl list_queues
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
