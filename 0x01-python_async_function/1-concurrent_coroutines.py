#!/usr/bin/env python3
"""Concurrent coroutines"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay and returns \
    the list of delays in ascending order"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delay_list = []

    for completed_coroutine in asyncio.as_completed(coroutines):
        delay = await completed_coroutine
        delay_list.append(delay)

    return delay_list
