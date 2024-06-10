#!/usr/bin/env python3
"""
Module
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    wait for a random amount of time and returns.

    Returns:
        a random float between 0 and the max_delay
    """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
