#!/usr/bin/env python3
"""A type-annotated function that converts it arguments to a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts arguments passed into a tuple

    Parameters:
        k (str): key
        v (int | float): value

    Returns:
        A tuple of @k and @v
    """

    return (k, v ** 2)
