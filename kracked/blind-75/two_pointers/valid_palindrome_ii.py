
def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def validPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try skipping either left or right character
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
        left += 1
        right -= 1
    return True

# Test cases
print(validPalindrome("aba"))  # True
print(validPalindrome("abca")) # True
print(validPalindrome("abc"))  # False
