#!/usr/bin/env python3
"""
Module to measure the total runtime
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure total execution time"""

    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start_time
