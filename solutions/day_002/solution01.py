def product_expect_self(nums: list) -> list:
    # Calculate the product of nums
    product = 1
    for num in nums:
        product *= num

    return [product // num for num in nums]
