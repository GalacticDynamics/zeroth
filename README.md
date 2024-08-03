<h1 align='center'> zeroth </h1>
<h2 align="center">Efficiently get the index-0 element of an iterable.</h2>

This is a micro-package, containing the single function `zeroth`. </br> `zeroth`
is syntactic sugar for `next(iter(obj))`, with a nice docstring.

## Installation

[![PyPI platforms][pypi-platforms]][pypi-link]
[![PyPI version][pypi-version]][pypi-link]

<!-- [![Conda-Forge][conda-badge]][conda-link] -->

```bash
pip install zeroth
```

## Documentation

[![Actions Status][actions-badge]][actions-link]

```python
from zeroth import zeroth

print(zeroth([0, 1, 2]))
# 0

print(zeroth((3, 2, 1)))
# 3

print(zeroth({"a": 1, "b": 2, "c": 3}))
# 'a'

print(zeroth(range(3)))
# 0

print(zeroth(range(1, 3)))
# 1

print(zeroth(map(str, range(3))))
# '0'

import numpy as np

print(zeroth(np.array([1, 2, 3])))
# 1


class ReverseIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(reversed(self.data))


print(zeroth(ReverseIterable([1, 2, 3])))
# 3
```

## Q&A

_Why isn't this called `first` since it gets the element with ordinality of 1?_

Because that package name is already taken on PyPI. Here zeroth refers to the
index.

<!-- SPHINX-START -->

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/GalacticDynamics/zeroth/workflows/CI/badge.svg
[actions-link]:             https://github.com/GalacticDynamics/zeroth/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/zeroth
[conda-link]:               https://github.com/conda-forge/zeroth-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/GalacticDynamics/zeroth/discussions
[pypi-link]:                https://pypi.org/project/zeroth/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/zeroth
[pypi-version]:             https://img.shields.io/pypi/v/zeroth

<!-- prettier-ignore-end -->
