#!/usr/bin/env python3
"""imports task wait random from previous file"""

import asyncio
from typint import List
task_wait_random = __import__('3-tasks.py').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Tasks 4"""
    delays: List[float] = []
    all_delays: List[float] = []
    [delays.append(task_wait_random(max_delay)) for i in range(n)]

    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)

    return all_delays
