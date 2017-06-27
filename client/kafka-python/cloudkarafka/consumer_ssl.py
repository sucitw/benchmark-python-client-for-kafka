# Consumer.py
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from settings import brokers, ssl_context, topic_prefix


# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(topic_prefix + 'default',
                         group_id='my-group',
                         bootstrap_servers=brokers,
                         security_protocol='SSL',
                         ssl_context=ssl_context)
print ('Start consuming')
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))