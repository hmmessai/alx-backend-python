#!/usr/bin/env python3
"""
Defines function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Generates a function that will act as a multiplier
    """
    def multiply(num: float) -> float:
        return float(num * multiplier)

    return multiply
