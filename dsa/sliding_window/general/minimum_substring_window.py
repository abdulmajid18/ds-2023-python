class Solution:
    def minWindowBruteForce(self, s: str, t: str) -> str:
        min_len = float('inf')
        min_window = ""
        s1_map = {}
        for char in t:
            if char in s1_map:
                s1_map[char] += 1
            else:
                s1_map[char] = 1
        print(s1_map)

        def contains_chars(s2):
            s2_map = {}
            for char in s2:
                if char in s2_map:
                    s2_map[char] += 1
                else:
                    s2_map[char] = 1

            for char, freq in s1_map.items():
                if s2_map.get(char, 0) < freq:
                    return False
            return True

        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if contains_chars(substring):
                    if len(substring) < min_len:
                        min_window = substring
                        min_len = len(substring)

        return min_window


class Solution2:
    def minWindowOptimized(self, s: str, t: str) -> str:
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

