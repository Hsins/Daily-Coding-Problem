## 題目敘述

The area of a circle is defined as ${\pi}r^2$. Estimate $\pi$ to `3` decimal places using a Monte Carlo method.

**Hint**: The basic equation of a circle is $x^2 + y^2 = r^2$.

## 解答

```python
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
```