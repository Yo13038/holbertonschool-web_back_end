#!/usr/bin/env python3
"""
Module collect 10 random number using async, return list
"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """list of all random number and return a list of them"""
    return [i async for i in async_generator()]
