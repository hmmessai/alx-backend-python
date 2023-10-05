#!/usr/bin/env python3
"""
Defines function sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Accepts mixed integer and float containing list
    and returns sum of all elements in float
    """
    result = 0.0
    for i in mxd_list:
        result += i
    return result
