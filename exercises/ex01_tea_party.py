"""Outputs the amount of tea bags, treats, and money required for a number of people"""

__author__ = 730487315


def tea_bags(people: int) -> int:
    """returns number of tea bags given number of people"""
    return 2 * people


def treats(people: int) -> int:
    """returns number of treats given number of people"""
    return int(tea_bags(people=people) * 1.5)


# calls tea_bags to reduce the amount of places in the code
# I would have to update if guests drank a different amount of teas than expected.


def cost(tea_count: int, treat_count: int) -> float:
    """calculates cost of treats and tea bags"""
    return tea_bags(people=6) * 0.50 + treats(people=6) * 0.75
