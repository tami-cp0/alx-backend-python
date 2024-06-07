#!/usr/bin/env python3
"""
Module to showcase type annotations
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """returns a tuple of the string & square of v as float"""
    return (k, float(v * v))
