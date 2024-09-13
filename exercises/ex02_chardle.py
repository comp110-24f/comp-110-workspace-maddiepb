"""Takes a word and a character and checks for instances of that letter in the word"""

__author__ = "730487315"


def main() -> None:
    """Puts together the programs functions"""
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """Prompts user for 5 character word and returns that word if input is valid"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:  # if word is not exactly 5 characters
        print("Error: Word must contain 5 characters.")
        exit()
    return word  # returns word only if if statement evaluates to False


def input_letter() -> str:
    """Prompts user for single character and returns that character if input is valid"""
    letter: str = input("Enter a single character: ")
    if len(letter) > 1:  # prints message if letter is more than one character
        print("Error: Character must be a single character.")
        exit()
    return letter  # returns letter only if if statement evaluates to False


def contains_char(word: str, letter: str) -> None:
    """Checks if word contains letter"""
    print("Searching for " + letter + " in " + word)
    count_match: int = (
        0  # initialize variable to count letters in word that match input
    )
    if word[0] == letter:
        print(letter + " found at index 0")
        count_match = count_match + 1  # adds 1 to count variable if match is found
    if word[1] == letter:
        print(letter + " found at index 1")
        count_match = count_match + 1  # adds 1 to count variable if match is found
    if word[2] == letter:
        print(letter + " found at index 2")
        count_match = count_match + 1  # adds 1 to count variable if match is found
    if word[3] == letter:
        print(letter + " found at index 3")
        count_match = count_match + 1  # adds 1 to count variable if match is found
    if word[4] == letter:
        print(letter + " found at index 4")
        count_match = count_match + 1  # adds 1 to count variable if match is found

    if count_match == 1:  # prints different messages depending on value of count_match
        print(str(count_match) + " instance of " + letter + " found in " + word)
    elif count_match > 1:
        print(str(count_match) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
