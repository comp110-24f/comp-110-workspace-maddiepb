"""Three functions that mutate or return list elements"""

__author__ = "730487315"


def get_first(list: list[str]) -> str:
    """return first element"""
    if len(list) == 0:
        return ""
    return list[0]


def remove_first(list: list[str]) -> None:
    """remove first element"""
    list.pop(0)


def get_and_remove_first(list: list[str]) -> str:
    """return and remove first element"""
    first: str = list[0]
    list.pop(0)
    return first
