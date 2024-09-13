"""Takes a word and a character and checks for instances of that letter in the word"""

__author__ = "730487315"


def input_word() -> str:
    word: str = input("Enter a five character word: ")
    if len(word) > 5 or len(word) < 5:
        print("Error: Word must contain 5 characters.")
    return word  # Not sure if I need to do this or remove print statements


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) > 1:
        print("Error: character must be a single character.")
    return letter  # Not sure if I need to do this or remove print statements


def contains_char(word, letter) -> None:
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        print(letter + " found at index 0")
    if word[1] == letter:
        print(letter + " found at index 1")
    if word[2] == letter:
        print(letter + " found at index 2")
    if word[3] == letter:
        print(letter + " found at index 3")
    if word[4] == letter:
        print(letter + " found at index 4")


contains_char(word=input_word(), letter=input_letter())
