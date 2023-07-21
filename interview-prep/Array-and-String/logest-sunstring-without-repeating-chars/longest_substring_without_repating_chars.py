class Solution:
    #  abcabcbb
    def longest_1(self, string):
        char_set = set()
        l = 0
        res = 0

        for r in range(len(string)):
            while string[r] in char_set:
                char_set.remove(string[l])
                l += 1
            char_set.add(string[r])
            res = max(res, r - l + 1)
        return res;