"""Practice with functions"""

# from random import randint

# print(randint(1, 10))


# defining a function
def sum(num1: int, num2: int) -> int:
    """Returns the sum of the arguments"""

    return num1 + num2


# call the function
print(
    sum(num1=1, num2=10)
)  # <- 1 and 10 are the arguments-- the specific values for a parameter
# sum(num1=randint(1,10), num2=randint(2,20))
