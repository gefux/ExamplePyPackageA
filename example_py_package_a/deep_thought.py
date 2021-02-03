# Copyright (c) 2021 Gerald E. Fux
#
# Licensed under the MIT License
"""
Here should be the short module description.

Here should be some more detailed description of the package.
"""
from typing import Tuple

from example_py_package_a.config import SACASTIC_DEEP_THOUGHT_ULTIMATE_ANSWER

def a_divided_by_b(a: int, b: int) -> Tuple[int, int]:
    """
    Performs an integer division.

    Given the integers `a` and `b` it returns `c` and `r` such that:
    `b * c  + r   == a`

    Parameters
    ----------
    a: int
        The dividend.
    b: int
        The divisor.

    Returns
    -------
    c: int
        The quotient.
    r: int
        The rest.
    """
    if b == 0:
        c = SACASTIC_DEEP_THOUGHT_ULTIMATE_ANSWER
        r = a
    else:
        c = a//b
        r = a%b
    return (c,r)
