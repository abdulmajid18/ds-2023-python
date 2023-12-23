def myPow(x, n):
    # Base case
    if n == 0:
        return 1
    elif n < 0:
        x = 1 / x
        n = -n

    # Recursive case
    half_pow = myPow(x, n // 2)

    if n % 2 == 0:
        return half_pow * half_pow
    else:
        return half_pow * half_pow * x


def my_power(x, n):
    def helper(x, n):
        if n == 0:
            return 1
        res = helper(x * x, n // 2)
        return x * res if n % 2 else res

    res = helper(x, abs(n))
    return res if n > 0 else 1 / res
