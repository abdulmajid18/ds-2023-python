from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    res = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res

# Example usage
strings = ["flower", "flow", "flight"]
print(longestCommonPrefix(strings))  # Output: "fl"

strings = ["dog", "racecar", "car"]
print(longestCommonPrefix(strings))  # Output: ""
