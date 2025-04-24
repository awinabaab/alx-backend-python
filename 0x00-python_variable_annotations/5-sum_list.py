#!/usr/bin/env python3
"""A type-annotated function that sums up a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums up a list of floats

    Parameters:
        input_list (List[float]): list of floats to sum up

    Returns:
        Sum of all values in @input_list
    """

    return sum(input_list)
