#!/usr/bin/env python3
"""Module for wait_n function with asyncio"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of delays in ascending order"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for response in asyncio.as_completed(tasks):
        result = await response
        delays.append(result)
    return delays
