#!/usr/bin/env python3

"""Module that defines to_kv function."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple containing k and the square of v."""
    return (k, v ** 2)
