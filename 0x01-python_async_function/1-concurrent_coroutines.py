#!/usr/bin/env python3
"""
Defines the asyncronous funtion wait_n
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates a list of wait_random process return
    with ascending order
    Returns: list of the outputs in ascending order
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
