"""Define several utility functions with dictionaries."""

__author__ = "730487315"

a: dict[str, str] = {"a": "b", "c": "d"}
b: list[str] = ["cake", "candle", "Birthday", "boy", "like"]
c: dict[str, list[str]] = {
    "Monday": ["Maggie", "Mildred"],
    "Tuesday": ["Guthrie"],
}
d: list[str] = ["dog", "dog", "cat", "letter", "letter", "letter"]
e: dict[str, str] = {
    "Marc": "yellow",
    "Ezri": "blue",
    "Kris": "blue",
    "Molly": "yellow",
}


def invert(values: dict[str, str]) -> dict[str, str]:
    """Iterates through input and adds value-key pairs to new dictionary."""
    inverted_values: dict[str, str] = {}
    for key in values:
        if values[key] in inverted_values:
            raise KeyError("")
        inverted_values[values[key]] = key
    return inverted_values


def favorite_color(fav_colors: dict[str, str]) -> str:
    """Finds and returns most popular color."""
    colors: list[str] = list()
    for key in fav_colors:
        colors.append(fav_colors[key])  # Creates a list with just the colors.

    tally: dict[str, int] = count(
        colors
    )  # Gives list of colors and the amount of times they appear in dict.
    max_count: int = 0
    max_color: str = ""

    for key in tally:  # Iterates through colors and instances.
        if tally[key] > max_count:  # Finds color with greatest count and returns it.
            max_count = tally[key]
            max_color = key
    return max_color


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of repeat elements in a list."""
    count: dict[str, int] = dict()
    for idx in range(0, len(values)):
        if values[idx] in count:
            count[values[idx]] += 1
        else:
            count[values[idx]] = 1
    return count


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Returns dictionary of list elements by their first character."""
    output: dict[str, list[str]] = {}

    for idx in range(0, len(input)):
        if input[idx][0].lower() in output:
            output[input[idx][0]].append(
                input[idx]
            )  # Append word from list to the list at key equal to first letter of word.
        else:
            output[input[idx][0].lower()] = [
                input[idx]
            ]  # Adds dictionary entry if not already existing--avoids KeyError.
    return output


def update_attendance(
    attendance: dict[str, list[str]], weekday: str, student: str
) -> None:
    """Updates dictionary of weekdays and students."""
    if weekday not in attendance:
        attendance[weekday] = [
            student
        ]  # Initializes list if list doesn't already exist.
    elif student not in attendance[weekday]:
        attendance[weekday].append(student)
