def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0] * 26, [0] * 26

    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord("a")] += 1
        s2Count[ord(s1[i]) - ord("a")] += 1

    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True
        index = ord(s2[r]) - ord('a')
        s1Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s1Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        l += 1

    return matches == 26

from collections import Counter


def checkInclusion2(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_count = Counter(s1)
    s2_count = Counter(s2[:len(s1)])

    for i in range(len(s1), len(s2)):
        if s1_count == s2_count:
            return True
        s2_count[s2[i]] += 1
        if s2_count[s2[i - len(s1)]] == 1:
            del s2_count[s2[i - len(s1)]]
        else:
            s2_count[s2[i - len(s1)]] -= 1

    return s1_count == s2_count


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    result = checkInclusion(s1, s2)
    print(result)  # Output: True
