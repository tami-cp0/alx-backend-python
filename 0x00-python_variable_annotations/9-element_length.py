#!/usr/bin/env python3
"""
Module to showcase type annotations
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function to demonstrate type annotation understanding.
    """
    return [(i, len(i)) for i in lst]
