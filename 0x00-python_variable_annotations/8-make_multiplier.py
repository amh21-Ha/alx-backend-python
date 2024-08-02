#!/usr/bin/env python3
"""
Module to create a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of the float and the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies the input value by the multiplier.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return value * multiplier

    return multiplier_function
