#!/usr/bin/env python
import pika
import sys

cred = pika.PlainCredentials(usename,password)
params = pika.ConnectionParameters(host,port,vhost,cred)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange=ex_name,
                exchange_type='direct',
                durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange=ex_name,
routing_key=q_name,
body=message)
print(" [x] Sent %r" % message)
connection.close()
