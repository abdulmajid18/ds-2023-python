def minStepsToAnagram(s1, s2):
    # Initialize dictionaries to store character frequencies
    freq_s1 = {}
    freq_s2 = {}

    # Count character frequencies in the first string
    for char in s1:
        freq_s1[char] = freq_s1.get(char, 0) + 1

    # Count character frequencies in the second string
    for char in s2:
        freq_s2[char] = freq_s2.get(char, 0) + 1

    # Calculate the minimum number of steps
    steps = 0
    for char in set(s1 + s2):
        steps += abs(freq_s1.get(char, 0) - freq_s2.get(char, 0))

    return steps


# Example usage:
s1 = "abc"
s2 = "acb"
result = minStepsToAnagram(s1, s2)
print(result)  # Output: 1
