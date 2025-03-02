def checkPermutationSorting(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


# Example Runs
print(checkPermutationSorting("listen", "silent"))  # True (Anagrams)
print(checkPermutationSorting("hello", "ollhe"))  # True (Permutations)
print(checkPermutationSorting("abc", "def"))  # False


def checkPermutationArray(s1, s2):
    if len(s1) != len(s2):
        return False

    char_count = [0] * 128

    for char in s1:
        char_count[ord(char)] += 1

    for char in s2:
        char_count[ord(char)] -= 1
        if char_count[ord(char)] < 0:
            return False

    return True
