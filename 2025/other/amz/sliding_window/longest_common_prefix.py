from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i, char in enumerate(strs[0]):
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]

        return strs[0]


def longest_common_prefix(strs):
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or strs[0][i] != s[i]:
                return res
            res += strs[0][i]
    return res
