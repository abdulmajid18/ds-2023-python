def isPalindromeBruteForce(x: int) -> bool:
    return str(x) == str(x)[::-1]


def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False  # Negative numbers & multiples of 10 (except 0) are not palindromes

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10


class Solution:
    def isPalindrome(self, x: int) -> bool:
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

            div //= 100

        return True


