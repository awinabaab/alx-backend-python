#!/usr/bin/env python3
"""A type-annotated function that sums up \
a mixed list of floats and integers"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums up a mixed list of floats and integers

    Paramters:
        mxd_list (List[Union[int, float]]): mixed list to sum up

    Returns:
        Sum of all values in @mxd_lst
    """

    return sum(mxd_lst)
