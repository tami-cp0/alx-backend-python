#!/usr/bin/env python3
"""
Module to showcase type annotations.
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    function  to showcase type annotations.
    """
    if key in dct:
        return dct[key]
    else:
        return default
