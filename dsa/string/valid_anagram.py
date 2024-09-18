def isAnagram(s, t):
    if len(s) != len(t):
        return False
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countS[t[i]] = 1 + countS.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True


def is_anagram(s: str, t: str) -> bool:
    # If lengths are different, they cannot be anagrams
    if len(s) != len(t):
        return False

    # Sort both strings and compare them
    return sorted(s) == sorted(t)

# Example usage
s1 = "listen"
s2 = "silent"
print(is_anagram(s1, s2))  # Output: True