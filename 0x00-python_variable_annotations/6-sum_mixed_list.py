#!/usr/bin/env python3
"""
Module that showcases type annotations.
"""
from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """
    Returns:
        Sum of values in mxd_lst
    """
    return sum(mxd_lst)
