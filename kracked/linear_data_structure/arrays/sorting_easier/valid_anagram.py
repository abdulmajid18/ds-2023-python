from collections import Counter


def isAnagramHashmap(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


def isAnagramSorting(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def isAnagramCount(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26

    for ch in s:
        count[ord(ch) - ord('a')] += 1
    for ch in t:
        count[ord(ch) - ord('a')] -= 1

    return all(c == 0 for c in count)
