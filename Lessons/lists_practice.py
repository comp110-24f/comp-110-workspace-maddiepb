"""practice with lists"""

my_numbers: list[float] = list()  # <- constructor. can also write = []

my_numbers.append(1.5)
my_numbers.append(2.3)

game_points: list[int] = [102, 86, 94]
game_points[2]  # indexing (also called subscription notation)
# python -m Lessons.<file_name>

# Modifying elements
game_points[1] = (
    72  # canNOT do this with strings, lists are a mutable type, strings are immutable
)
# Removing elements
game_points.pop(1)  # removes whatever is at index 1

game_points.append(74)


def display(list_num: list[int]) -> None:
     """displays a list sequentially. loops over input and displays every value""" 
    idx: int = 0  # local variable
    while len(list_num) > idx:
        print(list_num[idx])
        idx += 1


game_points.append(74)
display(game_points)
