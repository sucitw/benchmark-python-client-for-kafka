# -*- coding: utf-8 -*-
# Producer.py

from kafka import KafkaProducer
from kafka.errors import KafkaError
from settings import brokers, ssl_context, topic_prefix

producer = KafkaProducer(bootstrap_servers=brokers,
                         security_protocol='SSL',
                         ssl_context=ssl_context)

# Asynchronous by default
future = producer.send(topic_prefix + 'default', b'raw_bytes')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    pass
    

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)