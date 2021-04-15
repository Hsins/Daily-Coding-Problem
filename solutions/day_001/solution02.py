"""DAY-001 Two Sum.

Level:
    Easy

Company:
    This problem was recently asked by Google.

Description:
    Given a list of numbers and a number k, return whether any two numbers from
    the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is
    17.

    Bonus: Can you do this in one pass?
"""
from bisect import bisect_left
from typing import List


def two_sum(nums: List[int], target: int) -> bool:
    """Search After Sorting.

        Sort the original array to make the element in order. Then we can use
        searching to check remaing number added to be the target existed or
        not.

        TIME    : O(nlogn)
        SPACE   : O(1)

    Args:
        nums (List[int]): list of numbers
        target (int): expected sum of any two numbers

    Returns:
        bool: whether any two numbers from list `nums` add up to `target`.
    """
    # sort the original list
    nums.sort()

    # search the list in order
    for cur, num in enumerate(nums):
        add_num = target - num
        idx = binary_search(nums, add_num)

        # Check two more things:
        #   1. the binary search found the target
        #   2. the index should't be as same as current number
        #
        # We need to check lst[i + 1] and lst[i - 1] to see if there's another
        # number that's the same value as lst[i].
        if not idx:
            continue
        elif idx != cur:
            return True
        elif idx + 1 < len(nums) and nums[idx + 1] == add_num:
            return True
        elif idx - 1 >= 0 and nums[idx - 1] == add_num:
            return True

    return False


def binary_search(lst, ele):
    idx = bisect_left(lst, ele)
    if idx != len(lst) and lst[idx] == ele:
        return idx
    return None
