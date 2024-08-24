class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1

            half = power(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            x = 1 / x
            n = -n
        return power(x, n)


def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1.0

    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    current_product = x

    while n > 0:
        if n % 2 == 1:
            result *= current_product
        current_product *= current_product
        n //= 2

    return result
