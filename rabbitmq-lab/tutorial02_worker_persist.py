import time

from conn import channel


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    #  the same channel
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.queue_declare(queue='task_queue', durable=True)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='task_queue')

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()
