#!/usr/bin/env python3
"""Module for task_wait_random function with asyncio"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> List[float]:
    """Returns a list of asyncio tasks"""
    return asyncio.create_task(wait_random(max_delay))
