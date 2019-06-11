#!/usr/bin/env python
import pika
import time
cred = pika.PlainCredentials(username,password)
params = pika.ConnectionParameters(host,port,vhost,cred)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange=ex_name, exchange_type='direct',durable=True)
channel.queue_bind(exchange=ex_name, queue=q_name)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,queue=q_name)

channel.start_consuming()
