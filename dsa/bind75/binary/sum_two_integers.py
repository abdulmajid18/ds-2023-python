class Solution:
    def getSumBruteForce(self, a: int, b: int) -> int:
        while b > 0:
            a += 1
            b -= 1

        # If b is negative, decrement a and increment b
        while b < 0:
            a -= 1
            b += 1

        return a


def getSum(a, b):
    # 32 bits integer max
    MAX = 2 ** 31 - 1
    # Mask to get 32 bits
    mask = 2 ** 32 - 1

    while b != 0:
        # a XOR b gives the sum without carry
        # a AND b gives the carry, shift it left
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    # if a is negative, get a's two's complement
    return a if a <= MAX else ~(a ^ mask)


# Example usage:
print(getSum(1, 2))  # Output: 3


def sumTwoIntegers(a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    MAX = 0x7FFFFFFF  # Maximum positive value for 32-bit signed integer

    while b != 0:
        # Calculate sum without carrying
        sum_without_carry = (a ^ b) & mask

        # Calculate carry
        carry = ((a & b) << 1) & mask

        # Update a and b
        a, b = sum_without_carry, carry

    # If a is greater than MAX, it means the result is negative in 32-bit
    return a if a <= MAX else ~(a ^ mask)

