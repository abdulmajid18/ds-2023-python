def string_to_int(s: str):
    res = 0
    for i in s:
        if i != ' ':
            digit = ord(i) - ord('0')
            res = (res * 10) + digit
    return res

def string_best_case(s: str):
    i = 0
    n = len(s)
    max_int = (2**31) - 1
    min_int = -1 * (2**31)
    max = max_int // 10
    num = 0

    while i < n and s[i] == ' ':
        i += 1
    sign = 1
    if i < n and s[i] == '+':
        i += 1
    elif i < n and s[i] == '-':
        sign = -1
        i += 1
    while i < n and s[i] >= '0' and s[i] <= '9':
        digit = ord(s[i]) - ord('0')
        if num > max or num == max and digit > 7:
            if sign == 1:
                return 2**31 - 1
            else:
                return 2**31
        num = (num * 10) + digit
        i += 1
    return num * sign


# A simple Python3 program for
# implementation of atoi
import sys


def myAtoi(Str):
    sign, base, i = 1, 0, 0

    # If whitespaces then ignore.
    while (Str[i] == ' '):
        i += 1

    # Sign of number
    if (Str[i] == '-' or Str[i] == '+'):
        sign = 1 - 2 * (Str[i] == '-')
        i += 1

    # Checking for valid input
    while (i < len(Str) and
           Str[i] >= '0' and Str[i] <= '9'):

        # Handling overflow test case
        if (base > (sys.maxsize // 10) or
                (base == (sys.maxsize // 10) and
                 (Str[i] - '0') > 7)):
            if (sign == 1):
                return sys.maxsize
            else:
                return -(sys.maxsize)

        base = 10 * base + (ord(Str[i]) - ord('0'))
        i += 1

    return base * sign


# Driver Code
Str = list(" -123")


if __name__ == '__main__':
    ans = string_best_case('-123')
    print(ans)
    val = myAtoi(Str)

    print(val)
