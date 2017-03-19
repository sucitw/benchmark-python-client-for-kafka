# -*- coding: utf-8 -*-
"""
    benchmark.py
    ~~~~~~~~~~~~
    Implements and sets the benchmarking related variables and functions for various benchmarking testing.

"""

import time
import kafka_client.client_pykafka as pykafka1


producer_timings = {}
consumer_timings = {}

def calculate_thoughput(timing, n_messages=1000000, msg_size=100):
    print("Processed {0} messsages in {1:.2f} seconds".format(n_messages, timing))
    print("{0:.2f} MB/s".format((msg_size * n_messages) / timing / (1024*1024)))
    print("{0:.2f} Msgs/s".format(n_messages / timing))


producer_timings['pykafka_producer'] = pykafka1.pykafka_producer_performance()
calculate_thoughput(producer_timings['pykafka_producer'])
