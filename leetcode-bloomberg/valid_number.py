def is_number(s: str):
    i = 0
    n = len(str)

    while i < n and s[i] == ' ':
        i += 1

    if i < n and s[i] == '+' or s[i] == '-':
        i += 1

    is_numeric = False
    while i < n and s[i].isdigit():
        i += 1
        is_numeric = True

    if i < n and s[i] == '.':
        i += 1
        while i < n and s[i].isdigit():
            i += 1
            is_numeric = True
    while i < n and s[i] == ' ':
        i += 1
    return is_numeric and i == n


def is_number_exponential(s: str):
    i = 0
    n = len(str)

    while i < n and s[i] == ' ':
        i += 1

    if i < n and s[i] == '+' or s[i] == '-':
        i += 1

    is_numeric = False
    while i < n and s[i].isdigit():
        i += 1
        is_numeric = True

    if i < n and s[i] == '.':
        i += 1
        while i < n and s[i].isdigit():
            i += 1
            is_numeric = True

    while is_numeric and i < n and s[i] == 'e':
        i += 1
        if i < n and s[i] == '+' or s[i] == '-':
            i += 1
        while i < n and s[i].isdigit():
            i += 1
            is_numeric = True
    while i < n and s[i] == ' ':
        i += 1
    return is_numeric and i == n
