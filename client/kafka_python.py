# -*- coding: utf-8 -*-
"""
    kafka_python.py
    ~~~~~~~~~~~~
    benchmarking performance of kafka_python client

"""
import time
from kafka import KafkaProducer, KafkaConsumer
from .settings import bootstrap_servers, msg_count, msg_payload, topic_kp

topic = topic_kp

def python_kafka_producer_performance(topic=topic):
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    print("\n>>> Connect Kafka in {} by kafka-python as producer". format(bootstrap_servers))
    producer_start = time.time()

    for i in range(msg_count):
        producer.send(topic, msg_payload)

    producer.flush() # clear all local buffers and produce pending messages

    return time.time() - producer_start

def python_kafka_consumer_performance(topic=topic):

    print("\n>>> Connect Kafka in {} by kafka-python as consumer". format(bootstrap_servers))

    consumer = KafkaConsumer(
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset = 'earliest', # start at earliest topic
        group_id = None # do no offest commit
    )
    msg_consumed_count = 0

    consumer_start = time.time()
    consumer.subscribe([topic])
    for msg in consumer:
        msg_consumed_count += 1

        if msg_consumed_count >= msg_count:
            break

    consumer_timing = time.time() - consumer_start
    consumer.close()
    return consumer_timing
