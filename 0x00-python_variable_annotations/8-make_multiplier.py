#!/usr/bin/env python3
"""A type-annotated function that returns a function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by @multiplier"""

    def m_multiplier(a_multiplier: float) -> float:
        return a_multiplier * multiplier

    return m_multiplier
