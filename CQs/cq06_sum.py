"""Summing the elements of a list using different loops"""

__author__ = "730487315"


def w_sum(vals: list[float]) -> float:
    """Uses a while loop to return sum of a given list of floats"""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1

    return sum


def f_sum(vals: list[float]) -> float:
    """Uses a for...in... loop to return sum of a given list of floats"""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum
