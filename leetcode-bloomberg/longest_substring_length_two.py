
def length_of_longest_substring_two_distinct(s):
    if len(s) == 0:
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

        # If there are more than two distinct characters, move the left pointer
        while distinct_count > 2:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                distinct_count -= 1
                del char_count[left_char]
            left += 1

        # Update the maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage:
if __name__ == '__main__':
    s = "eceba"
    result = length_of_longest_substring_two_distinct(s)
    print(result)  # Output: 3 (the longest substring with at most two distinct characters is "ece")
