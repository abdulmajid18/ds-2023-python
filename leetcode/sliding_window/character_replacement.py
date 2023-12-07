def character_replacement(s, k):
    count = {}
    res = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - 1 + 1) - max(count.values()) > 2:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)

    return res


def character_replacement_optimized(s, k):
    count = {}
    res = 0

    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r - 1 + 1) - maxf > 2:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)

    return res