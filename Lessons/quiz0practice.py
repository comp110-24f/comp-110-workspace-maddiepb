"""
def make_jersey(name: str, num: int) -> str:
    print(name + " is num " + str(jersey_num(num=num)))
    return name + ":" + str(num + 1)


def jersey_num(num: int) -> int:
    return num + 1
"""

"""
def echo(word: str, time: int) -> str:
    return word * time


print(echo)
"""


def greet(name: str) -> str:
    return "I'm so happy to see you " + name + "!"
    print(
        "Hello "
        + name
        + ", your name starts with an "
        + name[0]
        + " and ends with an "
        + name[len(name) - 1]
    )


def main() -> None:
    print(greet(name="Molly"))

    # Example usage:


main()
