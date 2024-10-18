"""Tests find_max.py"""

from CQs.cq07.find_max import find_and_remove_max


__author__ = "730487315"


# use case returns expected value
def test_return() -> None:
    a: list[int] = [2, 5, 7, 9, 8, 4, 9]
    assert find_and_remove_max(a) == 9


def test_mutate() -> None:
    a: list[int] = [2, 5, 7, 9, 8, 4, 9]
    find_and_remove_max(a)
    assert a == [2, 5, 7, 8, 4]


def test_edge() -> None:
    b: list[int] = []
    assert find_and_remove_max(b) == -1
