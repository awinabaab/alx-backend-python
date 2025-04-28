#!/usr/bin/env python3
"""Async IO Basic Syntax"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay and returns the random delay value"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
