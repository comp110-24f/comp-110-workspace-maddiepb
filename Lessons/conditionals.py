"""9/9-9/11 practicing conditionals"""


def less_than_10(num: int) -> None:
    """tells us if num is less than 10"""
    dub: int = num * 2  # 14
    dub = dub - 1  # 13
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("This is the end of the function!")


# less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """returns meassage based on if alarm is going off"""
    if alarm:  # or: if alarm is True
        return "Wake up! Go to Comp110!"
    else:
        return "Keep sleeping. You deserve it"


def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter matches the first letter of word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


# print(check_first_letter(word="happy", letter="s"))

# 9/11


def get_weather_report() -> str:
    """takes user input and gives advice for different weathers"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


print(get_weather_report())
