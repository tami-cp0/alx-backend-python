#!/usr/bin/env python3
"""
Module
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    Returns:
        An asycnio.task object
    """
    return asyncio.create_task(wait_random(max_delay))
