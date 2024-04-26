#!/usr/bin/env python3
"""Module for async generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields a random number between 0 and 10 every second for 10 seconds"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
