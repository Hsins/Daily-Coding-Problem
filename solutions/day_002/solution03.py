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
    # Example: [1, 2, 3, 4, 5] -> [1, 1, 2, 6, 24]
    prefix_products = [1]
    for num in nums[:-1]:
        prefix_products.append(prefix_products[-1] * num)

    # Generate suffix products
    # Example: [1, 2, 3, 4, 5] -> [120, 60, 20, 5, 1]
    suffix_products = [1]
    for num in reversed(nums[1:]):
        suffix_products.append(suffix_products[-1] * num)
    suffix_products = suffix_products[::-1]

    # Generate result
    # Example: [1, 1, 2, 6, 24]         (prefix_products)
    #          [120, 60, 20, 5, 1]      (suffix_products)
    #       -> [120, 60, 40, 30, 24]    (multiples)
    return [pre * suf for pre, suf in zip(prefix_products, suffix_products)]
