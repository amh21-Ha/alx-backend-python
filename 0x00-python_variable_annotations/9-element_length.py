#!/usr/bin/env python3
"""
Module to calculate the length of each element in a list of sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element from the input
    list and its length.

    Args:
        lst (Iterable[Sequence]): A list of sequences (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
        a sequence and the length of that sequence.
    """
    return [(i, len(i)) for i in lst]
