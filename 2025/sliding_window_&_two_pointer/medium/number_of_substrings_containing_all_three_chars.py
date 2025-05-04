def numberOfSubstringsBruteForce(s: str) -> int:
    n = len(s)
    res = 0

    for i in range(n):
        freq = {'a': 0, 'b': 0, 'c': 0}
        for j in range(i, n):
            freq[s[j]] += 1
            if freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                res += 1  # substring s[i..j] is valid
    return res


def numberOfSubstringsSlidingWindow(s: str) -> int:
    from collections import defaultdict

    count = defaultdict(int)
    res = 0
    left = 0

    for right in range(len(s)):
        count[s[right]] += 1

        while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
            res += len(s) - right
            count[s[left]] -= 1
            left += 1

    return res
