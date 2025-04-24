#!/usr/bin/env python3
"""Annotate a provided function"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a generator expression containing a list of tuples"""

    return [(i, len(i)) for i in lst]
