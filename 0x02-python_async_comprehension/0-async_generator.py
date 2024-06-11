#!/usr/bin/env python3
"""
Module doc
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    A generator that yields a total of 10 float numbers
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0.0, 10.0)
