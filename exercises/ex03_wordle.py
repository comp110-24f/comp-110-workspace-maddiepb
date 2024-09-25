"""Another Wordle clone"""

__author__ = "730487315"

secret: str = "smoke"


def input_guess(secret_len: int) -> str:
    """prompts for input and checks that it is the right length"""
    guess: str = input(
        f"Enter a {len(secret)} letter word: "
    )  # supposed to be {secret_len}
    while len(guess) != len(secret):  # also supposed to be secret_len?
        guess = input("That wasn't 5 chars! Try again: ")
    return guess


def contains_char(secret: str, char: str) -> bool:
    """checks if string contains a character"""
    assert len(char) == 1  # raises an error if not true
    index: int = 0
    boo: bool = (
        False  # initializes variable as False, so that if a matching character
        # is not found, False is returned
    )
    while index < len(secret):
        if secret[index] == char:
            boo = True
        index += 1
    return boo


def emojified(guess: str, secret: str) -> str:
    """"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    key: str = ""
    while index < len(guess):
        if (
            guess[index] == secret[index]
        ):  # if character at that index matches letter in secret word at that position
            key += GREEN_BOX
        elif contains_char(
            secret, guess[index]
        ):  # if secret word contains the indexed letter of guess in any position
            key += YELLOW_BOX
        else:  # character is not in the secret word
            key += WHITE_BOX
        index += 1
    return key
