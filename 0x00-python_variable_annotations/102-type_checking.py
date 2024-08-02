#!/usr/bin/env python3
"""
Module to zoom an array by a given factor.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms in on the array by repeating each element `factor` times.

    Args:
        lst (Tuple[int, ...]): A tuple of integers.
        factor (int): The number of times to repeat each element.
        Defaults to 2.

    Returns:
        List[int]: A list with each element repeated `factor` times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
