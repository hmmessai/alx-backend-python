#!/usr/bin/env python3
"""
Defines the asyncronous funtion wait_n
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Creates a list of wait_random process return
    with ascending order
    Returns: list of the outputs in ascending order
    """
    wait_times = await asyncio.gather(
            *(wait_random(max_delay) for i in range(n))
    )

    return sorted(wait_times)
