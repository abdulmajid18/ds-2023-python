def length_of_longest_substring_k_brute_force(s: str, k: int) -> int:
    max_len = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            if len(set(s[i:j+1])) <= k:
                max_len = max(max_len, j - i + 1)
    return max_len


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # write your code here
        from collections import defaultdict
        if k == 0:
            return 0

        l = 0
        freq = defaultdict()
        res = 0
        for r in range(len(s)):
            freq[s[r]] += 1

            while len(freq) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res

