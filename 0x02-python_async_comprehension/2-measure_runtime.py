#!/usr/bin/env python3
"""Measure runtime of an async comprehension operation"""
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times in parallel and \
    measures the total runtime and returns it."""

    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    stop_time = time.perf_counter()

    return stop_time - start_time
