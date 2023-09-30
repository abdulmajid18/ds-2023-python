import math


def reverse_int(x: int):
    MIN = -2147483648
    MAX = 2147483647

    res = 0
    while x:
        digit = int(math.fmod(x, 10))
        x = int(x / 10)

        if res > MAX // 10 or res == MAX // 10 and digit > MAX % 10:
            return 0
        if res < MIN // 10 or res == MIN // 10 and digit <= MIN % 10:
            return 0
        res = (res * 10) + digit
    return res


def reverse(x):
    ret = 0
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    while x != 0:
        # Handle overflow/underflow
        if abs(ret) > INT_MAX // 10 or (abs(ret) == INT_MAX // 10 and x % 10 != 0):
            return 0

        ret = ret * 10 + x % 10
        x //= 10

    return ret

if __name__ == '__main__':
    ans = reverse(123)
    print(ans)