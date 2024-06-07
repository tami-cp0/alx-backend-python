#!/usr/bin/env python3
"""

"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns:
        A function that multiples the multiplier against a float
    """

    def multiply(multiplier: float) -> float:
        """
        Multiples multiplier against a float
        """
        return multiplier * multiplier

    return multiply
