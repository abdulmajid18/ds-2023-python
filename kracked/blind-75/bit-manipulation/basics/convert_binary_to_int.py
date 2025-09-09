def binary_to_int(input_str: str):
    result = 0
    for digit in input_str:
        result = result * 2 + int(digit)
    return result


def binary_to_int_two(binary_str):
    result = 0
    for i, digit in enumerate(reversed(binary_str)):
        result += int(digit) * (2 ** i)
    return result

print(binary_to_int("1010"))  # 10
print(binary_to_int("111"))   # 7


from functools import reduce

binary_str = "1010"
num = reduce(lambda acc, d: acc * 2 + int(d), binary_str, 0)
print(num)  # 10
