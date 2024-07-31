"""Copyright (c) 2024 Nathaniel Starkman. All rights reserved.

zeroth: Efficiently get the index-0 element of an iterable.
"""

__all__ = ["zeroth"]

from typing import Iterable, TypeVar

T = TypeVar("T")


def zeroth(x: Iterable[T], /) -> T:
    """Return index-0 element of an iterable.

    Examples
    --------
    >>> from zeroth import zeroth

    >>> zeroth([0, 1, 2])
    0

    >>> zeroth((3, 2, 1))
    3

    >>> zeroth({"a": 1, "b": 2, "c": 3})
    'a'

    >>> zeroth(range(3))
    0

    >>> zeroth(range(1, 3))
    1

    >>> zeroth(map(str, range(3)))
    '0'

    >>> import numpy as np
    >>> int(zeroth(np.array([1, 2, 3])))
    1

    >>> class ReverseIterable:
    ...     def __init__(self, data):
    ...         self.data = data
    ...     def __iter__(self):
    ...         return iter(reversed(self.data))
    >>> zeroth(ReverseIterable([1, 2, 3]))
    3

    """
    return next(iter(x))
