class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def is_palindrome(s):
            return s == s[::-1]

        if not s:
            return 0

        if is_palindrome(s):
            return 1

        return 2


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def is_palindrome(s):
            l = 0
            r = len(s) - 1

            while l <= r:
                if s[l] == s[r]:  # Fixed the comparison here
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        if not s:
            return 0

        if is_palindrome(s):
            return 1

        return 2


# Example usage
solution = Solution()
print(solution.removePalindromeSub("ababa"))  # Output: 1 (it's a palindrome)
print(solution.removePalindromeSub("abb"))  # Output: 2 (not a palindrome)
print(solution.removePalindromeSub("baabb"))  # Output: 2 (not a palindrome)
print(solution.removePalindromeSub("a"))  # Output: 1 (it's a palindrome)
print(solution.removePalindromeSub(""))  # Output: 0 (empty string)
