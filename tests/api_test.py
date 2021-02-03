# Copyright (c) 2021 Gerald E. Fux
#
# Licensed under the MIT License
"""
Tests for the deep_thought module
"""

import pytest

from example_py_package_a import a_divided_by_b

def test_a_divided_by_b():
    assert a_divided_by_b(7, 2) == (3, 1)
    assert a_divided_by_b(-7, 2) == (-4, 1)

def test_a_divided_by_b_spetial_case():
    c, r = a_divided_by_b(7, 0)
    assert r == 7
