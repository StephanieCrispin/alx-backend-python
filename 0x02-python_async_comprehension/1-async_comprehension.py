#!/usr/bin/env python3
"""Second Task"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Generates a list of floats"""
    result = [i async for i in async_generator()]
    return result
