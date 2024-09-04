def myAtoi(self, s: str) -> int:
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    #  tim leading whitespaces
    s = s.strip()

    if not s:
        return 0

    #  check sign
    sign = 1
    index = 0

    if s[0] == '-':
        sign = -1
        index += 1
    elif s[0] == '+':
        index += 1

    #  convert digits into integer
    result = 0
    while index < len(s) and s[index].isdigit():
        digit = int(s[index])

        #  check overflow/underflow
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN

        result = (result * 10) + digit
        index += 1

    return sign * result