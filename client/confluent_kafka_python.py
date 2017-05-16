# -*- coding: utf-8 -*-
"""
    confluent_kafka_python.py
    ~~~~~~~~~~~~
    benchmarking performance of confluent-kafka-python client

"""
import time
import confluent_kafka
from .settings import bootstrap_servers, msg_count, msg_payload, topic_ckp

topic = topic_ckp

def confluent_kafka_producer_performance(topic=topic):

    conf = {'bootstrap.servers': bootstrap_servers}
    producer = confluent_kafka.Producer(**conf)
    print("\n>>> Connect Kafka in {} by confluent-kafka-python as producer". format(bootstrap_servers))

    messages_to_retry = 0

    producer_start = time.time()
    for i in range(msg_count):
        try:
            producer.produce(topic, value=msg_payload)
        except BufferError as e:
            messages_to_retry += 1

    # hacky retry messages that over filled the local buffer
    for i in range(messages_to_retry):
        producer.poll(0)
        try:
            producer.produce(topic, value=msg_payload)
        except BufferError as e:
            producer.poll(0)
            producer.produce(topic, value=msg_payload)

    producer.flush()

    return time.time() - producer_start

import uuid

def confluent_kafka_consumer_performance(topic=topic):

    msg_consumed_count = 0
    conf = {'bootstrap.servers': bootstrap_servers,
            'group.id': uuid.uuid1(),
            'session.timeout.ms': 6000,
            'default.topic.config': {
                'auto.offset.reset': 'earliest'
            }
    }

    consumer = confluent_kafka.Consumer(**conf)
    print("\n>>> Connect Kafka in {} by confluent-kafka-python as consumer". format(bootstrap_servers))

    consumer_start = time.time()
    # This is the same as pykafka, subscribing to a topic will start a background thread
    consumer.subscribe([topic])

    while True:
        msg = consumer.poll(1)
        if msg:
            msg_consumed_count += 1

        if msg_consumed_count >= msg_count:
            break

    consumer_timing = time.time() - consumer_start
    consumer.close()
    return consumer_timing
