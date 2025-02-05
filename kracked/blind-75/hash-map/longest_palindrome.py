from collections import Counter


def longestPalindrome(s: str) -> int:
    char_count = Counter(s)
    length = 0
    has_odd = 0

    for count in char_count.values():
        if count % 2 == 1:
            length += count - 1
            has_odd = 1
        else:
            length += count

    return length + has_odd
