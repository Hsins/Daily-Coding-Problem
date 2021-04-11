class Solution:
    @staticmethod
    def car(pair):
        return pair(lambda a, b: a)

    @staticmethod
    def cdr(pair):
        return pair(lambda a, b: b)
