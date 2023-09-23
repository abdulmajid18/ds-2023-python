import string
import unittest
from collections import Counter


def clean_phrase(phrase):
    return [c for c in phrase.lower() if c in string.ascii_lowercase]


def is_palindrome_permutation_ascii(string):
    x = [0] * 128
    for i in string:
        ascii_char = ord(i)
        x[ascii_char] += 1
    print(x)
    count = 0
    for i in x:
        count += x[i] % 2

    return count <= 1


def is_palindrome_permutation(string):
    counter = Counter(clean_phrase(string))
    frequency = [x % 2 for x in counter.values()]
    sum_frequency = sum(frequency)
    return sum_frequency <= 1


# class Test(unittest.TestCase):
#     test_cases = [
#         ("aba", True),
#         ("aab", True),
#         ("abba", True),
#         ("aabb", True),
#         ("a-bba", True),
#         ("a-bba!", True),
#         ("Tact Coa", True),
#         ("jhsabckuj ahjsbckj", True),
#         ("Able was I ere I saw Elba", True),
#         ("So patient a nurse to nurse a patient so", False),
#         ("Random Words", False),
#         ("Not a Palindrome", False),
#         ("no x in nixon", True),
#         ("azAZ", True),
#     ]
#     testable_functions = [
#         is_palindrome_permutation,
#
#     ]
#
#     def test_pal_perm(self):
#         for f in self.testable_functions:
#             for [test_string, expected] in self.test_cases:
#                 assert f(test_string) == expected


if __name__ == "__main__":
    # unittest.main()
    ans = is_palindrome_permutation_ascii("aba")
    print(ans)
