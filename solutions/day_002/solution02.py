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
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = suffix_products[::-1]

    # Generate result
    ans = []
    for idx, _ele in enumerate(nums):
        if idx == 0:
            ans.append(suffix_products[idx + 1])
        elif idx == len(nums) - 1:
            ans.append(prefix_products[idx - 1])
        else:
            ans.append(prefix_products[idx - 1] * suffix_products[idx + 1])
    return ans
