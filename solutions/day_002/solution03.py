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
    # Example: [1, 1, 2, 6, 24]
    #          [120, 60, 20, 5, 1]
    #       => [120, 60, 40, 30, 24]
    return [x * y for x, y in zip(prefix_products, suffix_products)]
