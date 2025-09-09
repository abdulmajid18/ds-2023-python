def convert_to_binary(num):
    if num == 0:
        return "0"

    res = ""
    while num > 0:
        if num % 2 == 1:
            res += "1"
        else:
            res += "0"
        num //= 2

    return res[::-1]


def to_binary(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return "".join(reversed(bits))

print(to_binary(10))  # '1010'
