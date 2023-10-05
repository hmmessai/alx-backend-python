#!/usr/bin/env python3
"""
Defines function sum_list
"""


def sum_list(input_list: list[float]) -> float:
    """
    Computes the sum of every element in the input list
    Args:
        input_list(list of floats): the list to get the addends
    Return:
        Sum of all the elements inside the list
    """
    result = 0
    for i in input_list:
        result += i
    return result
