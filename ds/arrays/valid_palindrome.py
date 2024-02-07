class Solution:
    def is_valid_palindrome(self, s: str):
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
        return True

def isPalindrome(s:str):
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while l < r and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1

def alphaNum(c):
    return ((ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or
    (ord("0") <= ord(c) <= ord("9")))