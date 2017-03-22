# -*- coding: utf-8 -*-
"""
    settings.py
    ~~~~~~~~~~~~
    Implements and sets the benchmarking related variables and functions for various benchmarking testing.

"""


# settings
msg_count = 1000000
msg_size = 100
msg_payload = ('pycontw 2017' * 20).encode()[:msg_size]
bootstrap_servers = 'localhost:9092' # change if your brokers live else where


producer_timings = {}
consumer_timings = {}
