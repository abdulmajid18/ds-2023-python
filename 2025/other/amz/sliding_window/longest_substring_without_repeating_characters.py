class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        hash_set = set()
        for r, v in enumerate(s):
            while v in hash_set:
                hash_set.remove(s[l])
                l += 1

            res = max(res, r - l + 1)
            hash_set.add(v)
        return res

