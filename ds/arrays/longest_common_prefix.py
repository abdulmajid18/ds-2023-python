def longestCommonPrefix(strs):
    res = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res


strings = ["flow", "flight","flower"]
result = longestCommonPrefix(strings)
print(result)


def longestCommonPrefixTwo(strs):
    """This is quite intuitive"""
    res = ""
    char_comp = max(strs)
    for i in range(len(char_comp)):
        # "flight"
        for s in strs:
            # ["flight", "flow", "flower"]
            if s[i] != char_comp[i]:
                return res
        res += char_comp[i]
    return res


strings = ["flight", "flow", "flower"]
result = longestCommonPrefix(strings)
print(result)
