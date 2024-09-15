def isPowerOfTwo(n):
    if n <= 0:
        return False

    x = 1
    while x <= n:
        if x == n:
            return True
        x *= 2
    return False


def isPowerOfTwo2(n):
    if n <= 0:
        return False
    power = 1
    while power < n:
        power *= 2
    return power == n


def isPowerOfTwoShifting(n):
    if n <= 0:
        return False

    # Check if n is a power of two by shifting
    power = 1
    while power < n:
        power <<= 1  # Shift left by 1 (equivalent to multiplying by 2)

    return power == n


def isPowerOfTwoBitManipulation(n):
    """
    Approach 1: Bit Manipulation A number is a power of two if it has exactly one bit set in its binary
    representation (for positive integers). For example:
    2^0 = 1 → binary 0001
    2^1 = 2 → binary 0010
    2^2 = 4 → binary 0100
    To check this, you can use a bitwise trick:

    For any number that is a power of two, n & (n - 1) == 0 because subtracting 1 from n flips all the bits after the
    rightmost 1, which will zero out the number when you perform the bitwise AND operation.

    :param n:
    :return:
    """
    return n > 0 and (n & (n - 1)) == 0


def isPowerOfTwoShifting2(n):
    return n > 0 and ((1 << 30) % n) == 0
