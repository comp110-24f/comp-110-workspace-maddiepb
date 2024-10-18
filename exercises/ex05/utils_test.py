"""Tests behavior, returns, and edge cases of three functions from utils.py"""

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

__author__ = "730487315"


# test only_evens
def test_evens_return() -> None:
    """Tests output."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(a) == [2, 4, 6]


def test_evens_mutate() -> None:
    """Tests that input list is not mutuated."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    only_evens(a)
    assert a == [1, 2, 3, 4, 5, 6]


def test_evens_edge() -> None:
    """Tests that empty list is returned."""
    b: list[int] = []
    assert only_evens(b) == []


def test_evens_edge_neg() -> None:
    """Tests negative numbers."""
    c: list[int] = [-1, -2, -3, -4]
    assert only_evens(c) == [-2, -4]


# test sub
def test_sub_return() -> None:
    """Tests output."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(a, 1, 4) == [2, 3, 4]


def test_sub_mutate() -> None:
    """Tests that input list is not mutated."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    sub(a, 1, 4)
    assert a == [1, 2, 3, 4, 5, 6]


# edge cases
def test_sub_edge_start() -> None:
    """Tests that empty list is returned for invalid start."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(a, 7, 4) == []


def test_sub_edge_end_less() -> None:
    """Tests that empty list is returned for invalid (too small) end."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(a, 1, 0) == []


def test_sub_edge_end_more() -> None:
    """Tests that full list is returned for invalid (too big) end."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(a, 1, 9) == [2, 3, 4, 5, 6]


def test_sub_edge_empty() -> None:
    """Tests that empty list is returned."""
    d: list[int] = []
    assert sub(d, 1, 2) == []


# test add_at_index
def test_add_at_index_mutate() -> None:
    """Tests that fn does not mutate input list."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    add_at_index(a, 7, 3)
    assert a == [1, 2, 3, 7, 4, 5, 6]


def test_add_at_index_return() -> None:
    """Tests that fn returns type None."""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert add_at_index(a, 7, 3) is None


# edge cases
def test_add_at_index_edge_empty() -> None:
    """Tests that IndexError is raised for indexes out of rang of the list,"""
    b: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(
            b, 3, 4
        )  # checks that IndexError is raised when input_idx is greater than length of the list
