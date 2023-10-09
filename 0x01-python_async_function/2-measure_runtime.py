#!/usr/bin/env python3
"""
Defines the measure_time function
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

async def execute(n: int, max_delay: int) -> float:
    s


def measure_time(n: int, max_delay: int) -> float:
    """
    Computes the time needed to complete one operation
    """
    start = time.perf_counter()
    await wait_n(n, max_delay)
    end = time.perf_counter()

    return (end - start) / n
