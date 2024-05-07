#!/usr/bin/env python3
"""Firsy Task"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """A generator that yields random numbers bet 0 and 10"""
    for _ in range(10):
        asyncio.sleep(1)
        yield random.random() * 10
