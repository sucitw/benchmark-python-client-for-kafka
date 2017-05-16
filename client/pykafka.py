# -*- coding: utf-8 -*-
"""
    client_pykafka.py
    ~~~~~~~~~~~~
    benchmarking performance of pykafka client

"""
import time
from pykafka import KafkaClient
from .settings import bootstrap_servers, msg_count, msg_payload, topic_pk

topic = topic_pk

def pykafka_producer_performance(use_rdkafka=False,topic=topic):

    # Setup client
    client = KafkaClient(hosts=bootstrap_servers)
    topic = client.topics[topic.encode('UTF-8')]
    producer = topic.get_producer(use_rdkafka=use_rdkafka)
    print("\n>>> Connect Kafka in {} by pykafka as producer".
          format(bootstrap_servers))

    msgs_produced = 0
    produce_start = time.time()
    for i in range(msg_count):
        # Start producing
        producer.produce(msg_payload)

    producer.stop() # Will flush background queue
    print("produce {} message".format(msg_count))
    return time.time() - produce_start


def pykafka_consumer_performance(use_rdkafka=False, topic=topic):
    # Setup client
    client = KafkaClient(hosts=bootstrap_servers)
    topic = client.topics[topic.encode('UTF-8')]
    print("\n>>> Connect Kafka in {} by pykafka as consumer".
          format(bootstrap_servers))

    msg_consumed_count = 0

    consumer_start = time.time()
    # Consumer starts polling messages in background thread, need to start timer here
    consumer = topic.get_simple_consumer(use_rdkafka=use_rdkafka)

    while True:
        msg = consumer.consume()
        if msg:
            msg_consumed_count += 1

        if msg_consumed_count >= msg_count:
            break

    consumer_timing = time.time() - consumer_start
    consumer.stop()
    return consumer_timing
