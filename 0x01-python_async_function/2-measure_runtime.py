#!/usr/bin/env python3
"""Measures the total execution of concurrent coroutines"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time of wait_n"""
    start = time.perf_counter()
    delay_list = asyncio.run(wait_n(n, max_delay))
    stop = time.perf_counter()

    total_execution_time = (stop - start) / n
    return total_execution_time
