#!/usr/bin/env python3
"""
Module to showcase type annotations
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[float, int]) -> tuple[str, float]:
    """
    Returns:
        A tuple:
            First element: k as a string
            Second element: the square of v as a float
    """
    return (k, float(v**2))
