#!/usr/bin/env python3
"""
Module who loop 10 time to return random number
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """call, wait and yield result"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
