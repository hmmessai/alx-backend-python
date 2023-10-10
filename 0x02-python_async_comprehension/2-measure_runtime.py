#!/usr/bin/env python3
"""
Define measure_runtime coroutine
"""
import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times
    in parallel and returns the runtime
    """
    start = perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    runtime = perf_counter() - start

    return runtime
