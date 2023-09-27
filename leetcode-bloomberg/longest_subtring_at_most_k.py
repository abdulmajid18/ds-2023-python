def length_of_longest_substring_k_distinct(s, k):
    if k == 0:
        return 0

    # Initialize variables
    max_length = 0
    left = 0
    char_count = {}
    distinct_count = 0

    for right in range(len(s)):
        # Add the current character to char_count
        char = s[right]
        if char not in char_count:
            char_count[char] = 0
            distinct_count += 1

        char_count[char] += 1

        # If there are more than K distinct characters, move the left pointer
        while distinct_count > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                distinct_count -= 1
                del char_count[left_char]
            left += 1

        # Update the maximum length
        max_length = max(max_length, right - left + 1)

    return max_length


def length_of_longest_substring_two_distinct(s):
    count = [0] * 256  # Initialize an array to store character counts
    i = 0  # Left pointer
    num_distinct = 0  # Number of distinct characters
    max_len = 0  # Maximum length of the substring

    for j in range(len(s)):
        if count[ord(s[j])] == 0:
            num_distinct += 1
        count[ord(s[j])] += 1

        while num_distinct > 2:
            count[ord(s[i])] -= 1
            if count[ord(s[i])] == 0:
                num_distinct -= 1
            i += 1

        max_len = max(j - i + 1, max_len)

    return max_len


# Example usage:
s = "eceba"
k = 2
result = length_of_longest_substring_k_distinct(s, k)
print(result)  # Output: 3 (the longest substring with at most 2 distinct characters is "ece")
