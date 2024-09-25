"""Another Wordle clone"""

__author__ = "730487315"


def input_guess(secret_len: int) -> str:
    """prompts for input and checks that it is the right length"""
    guess: str = input(
        f"Enter a {secret_len} letter word: "
    )  # supposed to be {secret_len} because later
    # input_guess will be called with len(secret) as the arguement for secret_len
    while len(guess) != secret_len:
        guess = input(f"That wasn't {secret_len} chars! Try again: ")
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
    """outputs series of emojis indicating whether the guess contains letters that are
    in the secret word in the correct position"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    key: str = (
        ""  # initialize empty string to build string of emojis depending on input
    )
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


def main(secret: str) -> None:
    """controls main game loop"""
    turn: int = (
        1  # one instead of zero because I used <= in the conditional, so = 1
        # will result in the corrct number of turns
    )
    won: bool = False  # initialize boolean variable to track when player wins

    while turn <= 6 and won is False:
        print(f"== Turn {turn}/6 ==")
        guess: str = input_guess(
            len(secret)
        )  # local variable guess is output of function with arugment the length of the
        # secret word
        print(emojified(guess=guess, secret=secret))  # displays output of emojified
        if guess == secret:
            won = True  # causes loop to exit
            print(f"You won in {turn}/6 turns!")
        turn += 1
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
