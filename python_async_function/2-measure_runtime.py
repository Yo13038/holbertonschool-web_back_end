#!/usr/bin/env python3
"""
Module that measure the runtime
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """measure the total execution time for wait_n"""
    start_time = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.perf_counter()
    