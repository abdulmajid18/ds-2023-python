def getSum(a: int, b: int) -> int:
    while b > 0:
        a += 1
        b -= 1

    # If b is negative, decrement a and increment b
    while b < 0:
        a -= 1
        b += 1

    return a


def getSumBit(a: int, b: int) -> int:
    # 32-bit mask in hexadecimal
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF

    while b != 0:
        # XOR for addition without carry
        a = (a ^ b) & MASK
        b =  ((a & b) << 1) & MASK

    # Handle negative numbers
    return a if a <= INT_MAX else ~(a ^ MASK)


