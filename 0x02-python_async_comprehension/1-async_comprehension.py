#!/usr/bin/env python3
"""
Module doc
"""
import asyncio
import random
from typing import AsyncGenerator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    return [x async for x in async_generator()]
