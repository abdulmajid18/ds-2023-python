"""
Ask these two questions for clarifications

Key Points:
Division by Zero: In most programming languages, dividing by zero is undefined and typically results in a runtime error.
LeetCode problems generally assume valid input, so handling this case might not be necessary unless explicitly required.

Overflow Case (INT_MIN / -1): In a 32-bit integer system, the division of INT_MIN by -1 results in a value that
exceeds INT_MAX (overflow). The problem statement may not explicitly mention this, but handling it ensures that your
solution is robust and avoids overflow issues.

"""

class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for the maximum and minimum values of a 32-bit signed integer
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        # Handle special case: division by zero (although this case is not expected in LeetCode)
        if divisor == 0:
            return INT_MAX if dividend > 0 else INT_MIN

        # Handle special case: division of INT_MIN by -1 (which would overflow)
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Use absolute values for dividend and divisor to simplify the algorithm
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            # Find the largest multiple of divisor that can be subtracted from dividend
            multiple = 1
            temp_divisor = divisor

            # Double the temp_divisor until it's larger than the remaining dividend
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            # Subtract the largest found multiple of divisor from the dividend
            dividend -= temp_divisor
            # Add the multiple to the quotient
            quotient += multiple

        # Apply the determined sign to the quotient
        return sign * quotient


class Solution2:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        # Handle special case: division by zero
        if divisor == 0:
            return INT_MAX if dividend > 0 else INT_MIN

        # Handle special case: division of INT_MIN by -1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Take the absolute values to simplify the algorithm
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            # Find the largest multiple of divisor that can be subtracted from dividend
            multiple = 1
            temp_divisor = divisor

            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            dividend -= temp_divisor
            quotient += multiple

        return sign * quotient
