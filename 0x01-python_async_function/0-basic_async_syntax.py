#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits
for a random delay and returns that delay.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[float, int]:
    """
    Waits for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns the delay.

    Args:
        max_delay (int): The maximum delay time (default is 10).

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
