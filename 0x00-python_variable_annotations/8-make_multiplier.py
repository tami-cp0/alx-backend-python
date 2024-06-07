#!/usr/bin/env python3
"""
Module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns:
        A function that multiples the multiplier against a float
    """

    def multiply(number: float) -> float:
        """
        Multiples multiplier against a float
        """
        return multiplier * number

    return multiply
