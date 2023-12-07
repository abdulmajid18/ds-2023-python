def is_palindrome(x):
    # Special case: Negative numbers are not palindromes
    if x < 0:
        return False

    # Convert the integer to a string
    x_str = str(x)

    # Compare the string with its reverse
    return x_str == x_str[::-1]


# Example usage:
number = 121
result = is_palindrome(number)
print(result)


def is_palindrome_best(x):
    # Special case: Negative numbers are not palindromes
    if x < 0:
        return False

    original_number, reversed_number = x, 0

    while x > 0:
        # Extract the last digit
        digit = x % 10

        # Build the reversed number
        reversed_number = reversed_number * 10 + digit

        # Remove the last digit from the original number
        x //= 10

    # Check if the original number is equal to its reverse
    return original_number == reversed_number


# Example usage:
number = 121
result = is_palindrome_best(number)
print(result)


def isPalindromeBest(x):
    if x < 0:
        return False
    div = 1
    while x >= 10 * div:
        div *= 10

    while x:
        right = x % 10
        left = x // div

        if left != right:
            return False
        x = (x % div) // 10
        div = div / 100
    return True
