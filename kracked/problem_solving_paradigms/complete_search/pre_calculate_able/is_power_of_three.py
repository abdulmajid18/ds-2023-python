def isPowerOfThree(n: int) -> bool:
    if n <= 0:
        return False

    while n % 3 == 0:
        n //= 3

    return n == 1


def isPowerOfThree2(n: int) -> bool:
    if n <= 0:
        return False

    powers = set()
    result = 1
    power = 0

    # Keep generating powers of 3 until we exceed n
    while result <= n:
        result = 3 ** power
        powers.add(result)
        power += 1

    return n in powers

