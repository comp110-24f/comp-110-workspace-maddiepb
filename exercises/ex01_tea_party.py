"""Outputs the amount of tea bags, treats, and money required for a number of people"""

__author__ = 730487315


def main_planner(guests: int) -> None:
    """returns number of tea bags, treats, and cost of a party
    for user input number of people"""

    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


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
    return tea_count * 0.50 + treat_count * 0.75


# must call tea_bags and treats functions as arguments for the two parameters
# when calling the cost function, NOT when defining it

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
