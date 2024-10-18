"""Three functions that create list of even nums, subset of a list, and mutates a list
to add a num at index."""

__author__ = "730487315"


def only_evens(nums: list[int]) -> list[int]:
    """Creates a list of the even numbers in the input."""
    even_list: list[int] = []
    for elem in nums:
        if elem % 2 == 0:  # If elem is even.
            even_list.append(elem)  # Adds element to new list.
    return even_list


def sub(nums: list[int], start: int, end: int) -> list[int]:
    sub_list: list[int] = []
    if start < 0:  # Start is 0 at minimum.
        start = 0
    if end > len(nums) - 1:  # End is the end of the list at most.
        end = len(nums)
    # If start is beyond range of list, end is before list, or list is empty.
    if len(nums) == 0 or start >= len(nums) or end <= 0:
        return []  # Returns empty list.

    for idx in range(start, end):
        sub_list.append(nums[idx])  # Adds element at the index to the new list.
    return sub_list


def add_at_index(nums: list[int], elem: int, input_idx: int) -> None:
    if input_idx > len(nums) or input_idx < 0:
        raise IndexError("Index is out of bounds for the input list")

    if len(nums) > 0:
        nums.append(nums[len(nums) - 1])  # Duplicates last item in the list.
    else:
        nums.append(elem)
        return None

    idx: int = len(nums) - 1  # Idx starts iterating at the end of the list.

    while idx > input_idx:  # Until reach desired input idx.
        nums[idx] = nums[
            idx - 1
        ]  # Copies preceeding element to current element to move things to the right.
        idx -= 1

    nums[input_idx] = (
        elem  # Does this last so that a duplicate element is replaced
        # with desired number at input_idx.
    )
