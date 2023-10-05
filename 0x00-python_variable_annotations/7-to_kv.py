#!/usr/bin/env python3
"""
Defines funcion to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes in a string k and int or float v as arguments
    and returns a key value pair of those in tuple
    """
    return (k, float(v ** 2))
