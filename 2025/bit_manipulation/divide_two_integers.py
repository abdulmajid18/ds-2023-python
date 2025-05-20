class Solution:
    def divideSubtraction(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        sign = -1 if (dividend < 0) != (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1

        return sign * quotient


def divideBit(dividend: int, divisor: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # Edge case: overflow
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    negatives = 2
    if dividend > 0:
        dividend = -dividend
        negatives -= 1
    if divisor > 0:
        divisor = -divisor
        negatives -= 1

    quotient = 0

    while dividend <= divisor:
        power_of_two = 1
        value = divisor

        while value >= INT_MIN >> 1 and dividend <= value + value:
            value += value           # value <<= 1
            power_of_two += power_of_two  # power_of_two <<= 1

        dividend -= value
        quotient += power_of_two

    return quotient if negatives != 1 else -quotient