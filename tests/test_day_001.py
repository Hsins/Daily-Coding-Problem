class TestDay001(object):
    testcases = [
        (([], 1), False),               # boundary condition
        (([1], 1), False),              # only one elements
        (([-1, 1, 3, 5], 0), True),     # negative numbers
        (([10, 15, 3, 7], 17), True),
        (([2, 7, 11, 15], 9), True),
        (([3, 2, 4], 6), True),
        (([3, 2, 4, 1, 9], 12), True),
    ]

    def test_product_expect_self01(self):
        from solutions.day_001.solution01 import two_sum
        for (inputs, expected) in self.testcases:
            assert expected == two_sum(*inputs)

    def test_product_expect_self02(self):
        from solutions.day_001.solution02 import two_sum
        for (inputs, expected) in self.testcases:
            assert expected == two_sum(*inputs)

    def test_product_expect_self03(self):
        from solutions.day_001.solution03 import two_sum
        for (inputs, expected) in self.testcases:
            assert expected == two_sum(*inputs)
