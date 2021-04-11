from random import uniform


class Solution:
    def generate_point(self) -> tuple:
        return (uniform(-1, 1), uniform(-1, 1))

    def is_in_circle(self, coords: tuple) -> bool:
        return coords[0] * coords[0] + coords[1] * coords[1] < 1

    def estimate_pi(self, iterations: int) -> float:
        in_circle = 0
        for _ in range(iterations):
            if self.is_in_circle(self.generate_point()):
                in_circle += 1

        return 4 * in_circle / iterations


if __name__ == "__main__":
    solution = Solution()
    print(solution.estimate_pi(10))
    print(solution.estimate_pi(100))
    print(solution.estimate_pi(1000))
    print(solution.estimate_pi(10000))
    print(solution.estimate_pi(100000))
    print(solution.estimate_pi(1000000))
    print(solution.estimate_pi(10000000))
