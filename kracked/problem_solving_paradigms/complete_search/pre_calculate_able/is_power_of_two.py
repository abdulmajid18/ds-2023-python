def isPowerOfTwo(n: int) -> bool:
    powers = set()

    result = 1
    power = 0
    while result <= n:
        result = 2 ** power
        power += 1
        powers.add(result)

    return n in powers


def isPowerOfTwo2(n: int) -> bool:
    if n <= 0:
        return False

    while n % 2 == 0:
        n //= 2

    return n == 1

