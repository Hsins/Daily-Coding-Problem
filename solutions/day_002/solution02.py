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
    result = []
    for idx, ele in enumerate(nums):
        if idx == 0:
            result.append(suffix_products[idx + 1])
        elif idx == len(nums) - 1:
            result.append(prefix_products[idx - 1])
        else:
            result.append(prefix_products[idx - 1] * suffix_products[idx + 1])
    return result
