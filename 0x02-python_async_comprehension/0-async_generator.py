#!/usr/bin/env python3
"""
Define async_generator funciton
"""
import asyncio
import random


async def async_generator():
    """
    Yields 10 random number between 0 and 10
    with 1 second wait
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
