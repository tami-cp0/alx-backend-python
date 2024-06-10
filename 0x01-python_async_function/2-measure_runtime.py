#!/usr/bin/env python3
"""
Module with function that measures the total execution time for an
imported module wait_n(n, max_delay)
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns:
        Total execution time / n
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time / n
