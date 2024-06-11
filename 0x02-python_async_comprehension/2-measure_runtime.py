#!/usr/bin/env python3
"""
Module doc
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    runs async_comprehension 4 times
    Returns:
        The total execution time
    """
    start = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end = time.time()
    elapsed_time = end - start

    return elapsed_time
