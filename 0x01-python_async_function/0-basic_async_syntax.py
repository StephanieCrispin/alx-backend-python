#!/usr/bin/env python3
"""Contains a function that returns a random floating value"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """an asyncronous co routine that takes vlalue and 
    generates and returns a random floating point value
     between zero and that value"""
    delay_value: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay_value)
    return delay_value
