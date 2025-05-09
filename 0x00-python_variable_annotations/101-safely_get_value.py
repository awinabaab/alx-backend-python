#!/usr/bin/env python3
"""Duck typing annotation"""
from typing import Any, Union, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """Duck typing annotation"""
    if key in dct:
        return dct[key]
    else:
        return default
