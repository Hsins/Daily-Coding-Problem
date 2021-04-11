class TestDay002(object):
    testcases = [
        ([3, 2, 1], [2, 3, 6]),
        ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        ([5, 4, 3, 2, 1], [24, 30, 40, 60, 120])
    ]

    def test_product_expect_self01(self):
        from solutions.day_002.solution01 import product_expect_self
        for (inputs, expected) in self.testcases:
            assert expected == product_expect_self(inputs)

    def test_product_expect_self02(self):
        from solutions.day_002.solution02 import product_expect_self
        for (inputs, expected) in self.testcases:
            assert expected == product_expect_self(inputs)

    def test_product_expect_self03(self):
        from solutions.day_002.solution03 import product_expect_self
        for (inputs, expected) in self.testcases:
            assert expected == product_expect_self(inputs)

    def test_product_expect_self04(self):
        from solutions.day_002.solution04 import product_expect_self
        for (inputs, expected) in self.testcases:
            assert expected == product_expect_self(inputs)
