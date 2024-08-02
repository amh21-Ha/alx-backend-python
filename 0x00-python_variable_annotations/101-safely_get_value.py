#!/usr/bin/env python3
"""
Module to safely get a value from a dictionary with a default.
"""

from typing import Mapping, TypeVar, Any, Union

# Create a type variable that can be any type
T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Safely gets a value from a dictionary. If the key is not found, returns the default value.

    Args:
        dct (Mapping[Any, T]): A dictionary with keys of any type and values of type T.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None]): The value to return if the key is not found in the dictionary. Defaults to None.

    Returns:
        Union[T, None]: The value corresponding to the key if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
