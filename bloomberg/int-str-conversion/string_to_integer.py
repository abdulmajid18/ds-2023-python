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
    max_int = (2 ** 31) - 1
    min_int = -1 * (2 ** 31)
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
                return 2 ** 31 - 1
            else:
                return 2 ** 31
        num = (num * 10) + digit
        i += 1
    return num * sign


# A simple Python3 program for
# implementation of atoi
import sys




# Driver Code
Str = list(" -123")


def atoi(s):
    # Remove leading whitespaces
    s = s.lstrip()

    # Check for empty string
    if not s:
        return 0

    # Check for optional sign
    sign = 1
    if s[0] in ['+', '-']:
        sign = -1 if s[0] == '-' else 1
        s = s[1:]

    # Convert numerical characters to integer
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break  # Stop if a non-digit character is encountered

    # Apply sign and handle overflow/underflow
    result *= sign
    result = max(min(result, 2 ** 31 - 1), -2 ** 31)

    return result


# Example usage:
# input_str = "   -42"
# result = atoi(input_str)
# print(result)

if __name__ == '__main__':
    ans = atoi('-12 3')
    print(ans)

