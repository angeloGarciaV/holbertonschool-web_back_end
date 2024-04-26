#!/usr/bin/env python3
"""Module that defines element_length function."""

from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing a sequence and its length."""
    return [(i, len(i)) for i in lst]
