def remove_palindrome_sub(s):
    if not s: return 0

    l, r = 0, len(s)-1

    while l<r:
        if s[l] != s[r]: return 2
        l += 1
        r -= 1

    return 1


def removePalindromeSub(s):
    # Helper function to check if a string is a palindrome
    def is_palindrome(s):
        return s == s[::-1]

    # If the input string is empty, return 0 (no removals needed)
    if not s:
        return 0

    # If the input string is already a palindrome, return 1 (remove it in one step)
    if is_palindrome(s):
        return 1

    # If the input string is not a palindrome, we can remove all characters in 2 steps
    return 2

# Example usage:
s = "ababa"
result = removePalindromeSub(s)
print(result)  # Output: 1 (since "ababa" is a palindrome)
