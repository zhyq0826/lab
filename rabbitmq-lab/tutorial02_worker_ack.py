import time

from conn import channel


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    #  the same channel
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.queue_declare(queue='hello')
channel.basic_consume(callback, queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
