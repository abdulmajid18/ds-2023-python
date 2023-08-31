"""

Given a string S, find the longest palindromic substring in S. You may assume that the
maximum length of S is 1000, and there exists one unique longest palindromic substring.
Hint:
First, make sure you understand what a palindrome means. A palindrome is a string
which reads the same in both directions. For example, “aba” is a palindrome, “abc” is not

"""


class Solution:

    def longest_palindrome(self, string):
        result_len = 0
        result_str = ""

        max_length = len(string)

        for i in range(max_length):
            l = i
            r = i
            while l >= 0 and r < max_length and string[l] == string[r]:
                if (r - l) + 1 > result_len:
                    result_len = (r - l) + 1
                    result_str = string[l:r + 1]
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < max_length and string[l] == string[r]:
                if (r - l) + 1 > result_len:
                    result_len = (r - l) + 1
                    result_str = string[l:r + 1]
                l -= 1
                r += 1

        return result_str


def main():
    schema="a"
    table="b"
    x = f"* from {schema}.{table}"
    print(x)
    s = Solution()
    result = s.longest_palindrome("babad")
    print(result)


if __name__ == "__main__":
    main()
