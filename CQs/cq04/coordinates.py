"""defines function that prints inputs in coordinate format"""

__author__ = "730487315"


def get_coords(xs: str, ys: str) -> None:
    idxx: int = 0
    idxy: int = 0
    while idxx < len(xs):
        while idxy < len(ys):
            print(f"{xs[idxx]},{ys[idxy]}")
            idxy += 1
        idxy = 0
        idxx += 1
