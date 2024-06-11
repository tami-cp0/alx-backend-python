#!/usr/bin/env python3
"""
Module doc
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns:
        List of yielded values from async_generator
    """
    return [x async for x in async_generator()]
