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




