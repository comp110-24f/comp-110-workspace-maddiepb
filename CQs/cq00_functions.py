"""Practice defining functions"""

__author__ = "730487315"


def mimic(message: str) -> str:
    """Repeats input(message) back to user"""
    return message


def main() -> None:
    """Pulls together functions into main function"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    """Calls main"""
    main()
