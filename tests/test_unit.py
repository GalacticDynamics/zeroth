"""Unit tests."""

import numpy as np
import pytest

from zeroth import zeroth


@pytest.mark.parametrize(
    ("obj", "expected"),
    [
        ([1, 2, 3], 1),  # list
        ((1, 2, 3), 1),  # tuple
        (range(3), 0),  # range
        (range(1, 3), 1),  # range
        (map(str, range(3)), "0"),  # map object
        ({"a": 1, "b": 2, "c": 3}, "a"),  # dict
    ],
    ids=lambda x: type(x).__name__,
)
def test_builtin(obj, expected):
    """Test zeroth function."""
    assert zeroth(obj) == expected


def test_np():
    """Test zeroth function with numpy array."""
    obj = np.array([1, 2, 3])
    expected = 1
    assert zeroth(obj) == expected


def test_custom():
    """Test zeroth function with custom iterable."""

    class CustomIterable:
        def __init__(self, data):
            self.data = data

        def __iter__(self):
            return iter(reversed(self.data))

    obj = CustomIterable([1, 2, 3])
    expected = 3
    assert zeroth(obj) == expected
