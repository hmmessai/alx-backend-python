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
    lstOfTime = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        delay = await task
        lstOfTime.append(delay)
    return sorted(lstOfTime)
