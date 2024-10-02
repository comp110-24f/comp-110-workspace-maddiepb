"""Mutating functions."""

__author__ = "730487315"


def manual_append(list: list[int], int: int) -> None:
    """appends int to end of list"""
    list.append(int)


def double(list: list[int]) -> None:
    """multiples every item of list by 2 and mutates the list to those values"""
    idx: int = 0
    while idx < len(list):
        list[idx] *= 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = (
    list_1  # refers to same id in the heap,
    # any change to list_1 will be refelected in list_2
)


double(list_2)

print(list_1)
print(list_2)  # will print the same list
