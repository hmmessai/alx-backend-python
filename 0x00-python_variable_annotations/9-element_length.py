#!/usr/bin/env python3
"""
Annotation of a given function the proper way
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list with tuple for the list and its length
    """
    return [(i, len(i)) for i in lst]
