# -*- coding: utf-8 -*-
"""
    client_pykafka.py
    ~~~~~~~~~~~~
    Implements and sets the benchmarking related variables and functions for various benchmarking testing.

"""
import time
from pykafka import KafkaClient
from .settings import bootstrap_servers, msg_count, msg_payload

def pykafka_producer_performance(use_rdkafka=False):

    # Setup client
    client = KafkaClient(hosts=bootstrap_servers)
    topic = client.topics[b'pykafka-test-topic']
    producer = topic.get_producer(use_rdkafka=use_rdkafka)
    print("Connect Kafak in {} by pykafka". format(bootstrap_servers))

    msgs_produced = 0
    produce_start = time.time()
    for i in range(msg_count):
        # Start producing
        producer.produce(msg_payload)

    producer.stop() # Will flush background queue
    print("produce {} message".format(msg_count))
    return time.time() - produce_start
