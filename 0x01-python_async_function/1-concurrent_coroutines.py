#!/usr/bin/env python3
"""
Module
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns:
        list of n return values from wait_random()
    """
    result = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return result
