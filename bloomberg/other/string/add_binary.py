def addBinary(a: str, b: str) -> str:
    result = []  # To store the binary result
    carry = 0  # To store the carry from adding bits
    i, j = len(a) - 1, len(b) - 1  # Start from the end of both strings

    # Loop until both strings are processed or there is a carry left
    while i >= 0 or j >= 0 or carry:
        # Get the current digit from each string or 0 if index is out of bounds
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        # Sum the digits and the carry
        total = digit_a + digit_b + carry

        # Append the current bit to the result (0 or 1)
        result.append(str(total % 2))

        # Update carry (0 or 1)
        carry = total // 2

        # Move to the next digit
        i -= 1
        j -= 1

    # The result array is in reverse order, so reverse it and join to form a string
    return ''.join(reversed(result))


# Example usage:
a = "1010"
b = "1011"
print(addBinary(a, b))  # Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''

        carry = 0

        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digit_a = ord(a[i]) - ord('0') if i < len(a) else 0
            digit_b = ord(b[i]) - ord('0') if i < len(b) else 0

            total = digit_a + digit_b + carry
            char = str(total % 2)
            res = char + res

            carry = total // 2

        if carry:
            res = '1' + res

        return res



