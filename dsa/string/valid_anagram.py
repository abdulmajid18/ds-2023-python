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


def is_anagram(s: str, t: str) -> bool:
    # If lengths are different, they cannot be anagrams
    if len(s) != len(t):
        return False

    # Create an array of size 26 for each string's character count
    count = [0] * 26

    # Count the frequency of characters in both strings
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    # If all counts are zero, they are anagrams
    return all(c == 0 for c in count)


# Example usage
s1 = "listen"
s2 = "silent"
print(is_anagram(s1, s2))  # Output: True
