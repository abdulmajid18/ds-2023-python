def int_to_string(x):
    is_negative = False

    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        char = ord('0') + x % 10
        s.append(chr(char))
        x //= 10
        if x == 0:
            break
    return ('-' if is_negative else '') + ''.join(reversed(s))