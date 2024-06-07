#!/usr/bin/env python3
"""
Module that showcases type annotations.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns:
        Sum of values in mxd_lst
    """
    return float(sum(mxd_lst))
