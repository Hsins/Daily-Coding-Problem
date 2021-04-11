def product_expect_self(nums: list) -> list:
    # Allocate memory for the product array
    result = [1] * len(nums)

    # Multiply the result array with products of prefix side
    # Example: [1, 2, 3, 4, 5] -> [1, 1, 2, 6, 24]
    temp = 1
    for idx, num in enumerate(nums):
        result[idx] = temp
        temp *= num

    # Multiply the result array with products of suffix side
    # Example: [1, 1, 2, 6, 4] -> [120, 60, 40, 30, 24]
    temp = 1
    for idx, num in enumerate(reversed(nums), start=1):
        result[-idx] *= temp
        temp *= num

    return result
