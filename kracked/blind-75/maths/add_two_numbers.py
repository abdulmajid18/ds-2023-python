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



