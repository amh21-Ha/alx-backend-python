#!/usr/bin/env python3
"""
Module to create a tuple containing a string and the square of an integer or float.
"""

from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple where the first element is a string and the second element is
    the square of the integer or float.

    Args:
        k (str): A string value.
        v (Union[int, float]): An integer or float value.

    Returns:
        Tuple[str, float]: A tuple with the string and the square of the value as float.
    """
    return (k, float(v ** 2))
