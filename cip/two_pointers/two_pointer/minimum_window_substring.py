from collections import Counter


def minWindowBruteForce(s: str, t: str) -> str:
    if not t or not s:
        return ""

    t_count = Counter(t)
    min_len = float('inf')
    result = ""

    for l in range(len(s)):
        window_count = Counter()
        for r in range(l, len(s)):
            window_count[s[r]] += 1

            if all(window_count[char] >= t_count[char] for char in t_count):
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    result = s[l:r + 1]
                break
    return result


def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""

    count_t, window = {}, {}
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    have, need = 0, len(count_t)
    min_len = float("inf")
    min_window = [-1, -1]
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1

        if c in count_t and window[c] == count_t[c]:
            have += 1

        while have == need:
            if (r - l + 1) < min_len:
                min_window = [l, r]
                min_len = (r - l + 1)

            # pop from left of our window
            window[s[l]] -= 1
            if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                have -= 1
            l += 1

    l, r = min_window
    return s[l:r + 1] if min_len != float("inf") else ""
