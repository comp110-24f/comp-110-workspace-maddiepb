"""Defines a funciton that finds and removes the max num in a list."""

__author__ = "730487315"

a: list[int] = [1, 8, 8, 2, 3, 8, 3]


def find_and_remove_max(nums: list[int]) -> int:
    """Returns biggest number and deletes all instances of it in a list."""
    idx: int = 0
    if nums == []:
        max_num = -1
        return max_num  # Returns -1 for an empty list and exits function.
    else:
        max_num: int = nums[0]  # initializes variable if list is not empty
    # Finds max number.
    for elem in nums:
        if elem > max_num:
            max_num = elem

    # Deletes all instances of max number in the list.
    while idx < len(
        nums
    ):  # While loop because for...in... with range function takes initial length
        # --len(nums)--and when popping values, the idx will be out of range.
        if nums[idx] == max_num:
            nums.pop(idx)
            idx -= 1
        idx += 1
    return max_num


find_and_remove_max(a)
print(a)
