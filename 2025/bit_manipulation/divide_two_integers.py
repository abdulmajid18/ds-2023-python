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
    # Handle overflow case
    if dividend == -2 ** 31 and divisor == -1:
        return 2 ** 31 - 1

    sign = -1 if (dividend > 0) ^ (divisor > 0) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0

    while dividend >= divisor:
        # Find the largest power of 2 multiplier
        temp_divisor, multiplier = divisor, 1
        while temp_divisor << 1 <= dividend:
            temp_divisor <<= 1
            multiplier <<= 1

        # Subtract and accumulate the quotient
        dividend -= temp_divisor
        quotient += multiplier

    return sign * quotient