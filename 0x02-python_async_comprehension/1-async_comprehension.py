#!/usr/bin/env python3
"""
Define an async_comprehension function
"""
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collect 10 random numbers using async_generator
    and return the 10 random numbers
    """
    return [i async for i in async_generator()]
