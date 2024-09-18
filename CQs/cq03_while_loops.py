"""Practice with while loops."""

__author__ = "730487315"


def num_instances(phrase: str, search_char: str) -> int:
    """takes phrase and a single character and searches the phrase for the character"""
    count: int = 0
    index: int = len(phrase) - 1
    while index >= 0:  # searches string from the end to the start
        if phrase[index] == search_char:
            count += 1
        index -= (
            1  # decreases index with each loop to move to next character in the string
        )
    return count
