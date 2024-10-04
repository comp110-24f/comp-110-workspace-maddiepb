"""Practice defining functions with lists."""

__author__ = "730487315"


def all(list: list[int], num: int) -> bool:
    """Iterates through list and checks if all items are equal to a given int."""
    idx: int = 0
    if len(list) == 0:  # Returns false for empty list.
        return False
    while idx < len(list):
        if list[idx] != num:
            return False
        idx += 1
    return True


def max(list: list[int]) -> int:
    """Iterates through items in a list and returns largest one."""
    idx: int = 0
    max_num: int = list[
        idx
    ]  # Initializes max var as first item in list, NOT 0 bc then neg nums won't work.
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    while idx < len(list):
        if list[idx] > max_num:
            max_num = list[idx]  # Updates max if higher value is found.
        idx += 1
    return max_num


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Checks if two lists are identical."""
    idx = 0
    if len(list_one) != len(list_two):
        return False
    while idx < len(
        list_one
    ):  # Doesn't matter which list var bc I check they are equal length.
        if list_one[idx] != list_two[idx]:
            return False
        idx += 1
    return True


def extend(list_one: list[int], list_two: list[int]) -> None:
    """Adds list_two to the end of list_one."""
    idx = 0
    while idx < len(list_two):
        list_one.append(list_two[idx])  # Adds each item of list_two every loop.
        idx += 1
