def isPalindromeBrute(x: int) -> bool:
    # Convert the number to a string
    s = str(x)
    # Reverse the string
    reversed_s = s[::-1]
    # Compare the original string with the reversed string
    return s == reversed_s


# Example usage
print(isPalindromeBrute(121))  # Output: True
print(isPalindromeBrute(-121))  # Output: False
print(isPalindromeBrute(10))  # Output: False


def isPalindrome(x: int) -> bool:
    # Special cases:
    # As mentioned, when x < 0, x is not a palindrome.
    # Also if the last digit of the number is 0, the first digit
    # must also be 0, so only 0 satisfies this property.
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # When the length is an odd number, we can get rid of the middle digit by reversed_half // 10
    # For example when the input is 12321, at the end of the loop we get x = 12, reversed_half = 123,
    # since the middle digit doesn't matter in palindrome (it will always equal to itself), we can simply get rid of it.
    return x == reversed_half or x == reversed_half // 10


# Example usage
print(isPalindrome(121))  # Output: True
print(isPalindrome(-121))  # Output: False
print(isPalindrome(10))  # Output: False
print(isPalindrome(12321))  # Output: True
