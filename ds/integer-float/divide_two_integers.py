def divide(dividend, divisor):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if dividend == 0:
        return 0

    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0

    while dividend >= divisor:
        # Find the largest multiple of divisor (shiftedDivisor) that is less than or equal to dividend
        shiftedDivisor, multiple = divisor, 1
        while dividend >= (shiftedDivisor << 1):
            shiftedDivisor <<= 1
            multiple <<= 1

        # Subtract shiftedDivisor from dividend and update quotient
        dividend -= shiftedDivisor
        quotient += multiple

    return sign * quotient

# Example usage:
dividend = 10
divisor = 3
result = divide(dividend, divisor)
print(result)
