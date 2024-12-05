from typing import List


def multiply(a: List, b: List):
    sign = -1 if (a[0] < 0) ^ (b[0] < 0) else 1
    a[0], b[0] = abs(a[0]), abs(b[0])

    res = [0] * (len(a) + len(b))

    for i in reversed(range(len(a))):
        for j in reversed(range(len(b))):
            product = a[i] * b[i]
            pos = i + j + 1
            res[pos] += product
            res[pos - 1] += res[pos] // 10
            res[pos] %= 10

    while len(res) > 1 and res[0] == 0:
        res.pop(0)

    if sign == -1:
        res[0] = -res[0]

    return res


def multiply_arrays(num_a, num_b):
    # Determine the sign of the result
    sign = -1 if (num_a[0] < 0) ^ (num_b[0] < 0) else 1

    # Convert to positive numbers for easier handling
    num_a = [abs(x) for x in num_a]
    num_b = [abs(x) for x in num_b]

    # Initialize a result array of appropriate length (max possible digits)
    res = [0] * (len(num_a) + len(num_b))

    # Perform multiplication
    for i in reversed(range(len(num_a))):
        for j in reversed(range(len(num_b))):
            res[i + j + 1] += num_a[i] * num_b[j]
            res[i + j] += res[i + j + 1] // 10  # Carry over
            res[i + j + 1] %= 10  # Keep only the last digit

    start = next((i for i, x in enumerate(res) if x != 0), len(res))
    res = res[start:] or [0]

    # Remove leading zeros
    while len(res) > 1 and res[0] == 0:
        res.pop(0)

    # Add the sign to the most significant digit
    if sign == -1:
        res[0] = -res[0]

    return res


# Example input
num1 = [1, 9, 3, 7, 0, 7, 7, 2, 1]
num2 = [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]

# Output the result
result = multiply_arrays(num1, num2)
print(result)
