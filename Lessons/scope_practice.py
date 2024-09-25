"""Practicing with global vs. local variables"""


def remove_chars(msg: str, char: str) -> str:
    """return a copy of msg with char removed"""
    copy: str = ""  # set up empty string we can copy onto
    index: int = 0  # local variables
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
        index += 1
    return copy


if (
    __name__ == "__main__"
):  # if runnign this file directly,run this code. otherwise, dont
    word: str = "yoyo"  # global variable
    print(remove_chars(word, "y"))
    print(remove_chars(word, "o"))
