#!/usr/bin/env python3
"""
Adding type annotations to the function
"""
from typing import Mapping, Any, Union, NoneType


def safely_get_value(dct: Mapping[], key: Any, default = None) -> Union[Any, ]:
    if key in dct:
        return dct[key]
    else:
        return default
