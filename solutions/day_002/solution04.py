"""DAY-002 Product of Array Except Self.

Level:
    Hard

Company:
    This problem was recently asked by Google.

Description:
    Given an array of integers, return a new array such that each element at
    index i of the new array is the product of all the numbers in the original
    array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be
    [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output
    would be [2, 3, 6].
"""


def product_expect_self(nums: list) -> list:
    # Allocate memory for the product array
    ans = [1] * len(nums)

    # Multiply the result array with products of prefix side
    # Example: [1, 2, 3, 4, 5] -> [1, 1, 2, 6, 24]
    temp = 1
    for idx, num in enumerate(nums):
        ans[idx] = temp
        temp *= num

    # Multiply the result array with products of suffix side
    # Example: [1, 1, 2, 6, 4] -> [120, 60, 40, 30, 24]
    temp = 1
    for idx, num in enumerate(reversed(nums), start=1):
        ans[-idx] *= temp
        temp *= num

    return ans
