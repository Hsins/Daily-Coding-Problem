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


from typing import List


def two_sum(nums: List[int], target: int) -> bool:
    """Nested Iteration (brute force).

        The brute force way to use nested iteration checking for every pair of
        numbers.

        TIME    : O(n^2)
        SPACE   : O(1)

    Args:
        nums (List[int]): list of numbers
        target (int): expected sum of any two numbers

    Returns:
        bool: whether any two numbers from list `nums` add up to `target`.
    """
    for outer_idx, outer_num in enumerate(nums):
        for inner_idx, inner_num in enumerate(nums):
            if outer_idx != inner_idx and outer_num + inner_num == target:
                return True

    return False
