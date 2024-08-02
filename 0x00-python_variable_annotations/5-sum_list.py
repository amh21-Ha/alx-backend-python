#!/usr/bin/env python3
"""
Module to calculate the sum of a list of floats.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of all the floats in a list.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the floats in the list.
    """
    return sum(input_list)
