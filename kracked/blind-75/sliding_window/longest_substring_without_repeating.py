def length_of_longest_substring_brute_force(s):
    def all_unique(substring):
        return len(substring) == len(set(substring))

    n = len(s)
    max_length = 0

    for i in range(n):
        for j in range(i + 1, n+1):
            print(j)
            if all_unique(s[i:j]):
                max_length = max(max_length, j - i)

    return max_length


# Example usage:
#  it O(n^3)
s = "abcabcbb"
print(s[0:2])
result = length_of_longest_substring_brute_force(s)
print("Length of the longest substring without repeating characters:", result)


def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()
    l = 0
    result = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        result = max(result, r - l + 1)
    return result