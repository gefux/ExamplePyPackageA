# Copyright (c) 2021 Gerald E. Fux
#
# Licensed under the MIT License
"""
An example Python 3 package (A).

Here should be some more detailed description of the package.
"""
from example_py_package_a.version import __version__

# all API functionallity is in __all__
# this is what you get if you import "*" from the package
__all__ = [
    'a_divided_by_b',
    ]

from example_py_package_a.deep_thought import a_divided_by_b
