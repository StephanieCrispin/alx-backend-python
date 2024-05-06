#!/usr/bin/env python3
"""imports wait random from previous file"""

import asyncio
from typint import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """runs wait random n times and returns the result"""
    delays: List[float] = []
    all_delays: List[float] = []
    [delays.append(wait_random(max_delay)) for i in range(n)]

    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)

    return all_delays
