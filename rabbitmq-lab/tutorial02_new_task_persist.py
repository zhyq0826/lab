import sys
from conn import channel
import pika


# This queue_declare change needs to be applied to both the producer and consumer code.
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                        delivery_mode=2,    # make message persistent
                    ))

print(" [x] Sent %r" % message)
