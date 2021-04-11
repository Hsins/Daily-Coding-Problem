# from solutions.DAY_0005_Function_car_cdr_and_cons.solution import Solution

# solution = Solution()
# car_test_data = [((3, 4), 3),
#                  (('first', 'last'), 'first'),
#                  ((['f', 'i', 'r', 's', 't'], ['l', 'a', 's', 't']), ['f', 'i', 'r', 's', 't'])]
# cdr_test_data = [((3, 4), 4),
#                  (('first', 'last'), 'last'),
#                  ((['f', 'i', 'r', 's', 't'], ['l', 'a', 's', 't']), ['l', 'a', 's', 't'])]


# # Given the implementation of cons
# def cons(a, b):
#     def pair(f):
#         return f(a, b)

#     return pair


# class TestSolution:
#     def test_car(self):
#         for (testcase, expected) in car_test_data:
#             assert expected == solution.car(cons(*testcase))

#     def test_cdr(self):
#         for (testcase, expected) in cdr_test_data:
#             assert expected == solution.cdr(cons(*testcase))
