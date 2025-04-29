#!/usr/bin/env python3
"""Async comprehension"""
from typing import List
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Comprehend the values yielded by async_generator"""

    return [number async for number in async_generator()]
