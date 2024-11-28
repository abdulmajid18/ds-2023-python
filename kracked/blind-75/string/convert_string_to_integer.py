def myAtoi(s: str) -> int:
    # Initialize variables
    i, n = 0, len(s)
    sign = 1
    result = 0

    # Skip leading whitespaces
    while i < n and s[i] == ' ':
        i += 1

    # Handle sign
    if i < n and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1

    # Convert digits
    while i < n and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1

    # Apply sign
    result *= sign

    # Clamp to 32-bit integer range
    INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX

    return result


def myAtoiCorrect(self, s: str) -> int:
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