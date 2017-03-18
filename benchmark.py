# -*- coding: utf-8 -*-
"""
    benchmark.py
    ~~~~~~~~~~~~
    Implements and sets the benchmarking related variables and functions for various benchmarking testing.

"""

import time

msg_count = 1000000
msg_size = 100
msg_payload = ('pycontw 2017' * 20).encode()[:msg_size]


producer_timings = {}
consumer_timings = {}

def calculate_thoughput(timing, n_messages=1000000, msg_size=100):
    print("Processed {0} messsages in {1:.2f} seconds".format(n_messages, timing))
    print("{0:.2f} MB/s".format((msg_size * n_messages) / timing / (1024*1024)))
    print("{0:.2f} Msgs/s".format(n_messages / timing))
