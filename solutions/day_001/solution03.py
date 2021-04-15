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
    """Hashing.

        Traverse the numbers and remember the nubmers we've seen. And what we
        should check is if there is another number added to be the target.

        Take [10, 15, 3, 7] for example:

            (1) num = 10, seen_num = ()         , target - num = 7
            (2) num = 15, seen_num = (10)       , target - num = 2
            (3) num = 3 , seen_num = (10, 15)   , target - num = 14
            (4) num = 7 , seen_num = (10, 15, 3), target - num = 10 (Match!)

        TIME    : O(n)
        SPACE   : O(n)

    Args:
        nums (List[int]): list of numbers
        target (int): expected sum of any two numbers

    Returns:
        bool: whether any two numbers from list `nums` add up to `target`.
    """
    seen_num = set()
    for num in nums:
        if target - num in seen_num:
            return True
        seen_num.add(num)
    return False
