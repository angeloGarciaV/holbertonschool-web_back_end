#!/usr/bin/env python3
"""Module that defines make_multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""
    def mult(n:  float) -> float:
        """Returns the product of a float and multiplier."""
        return n * multiplier
    return mult
