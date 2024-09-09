def lengthOfLongestSubstringTwoDistinct(s):
    # Edge case: If the string has less than 3 characters, return its length
    if len(s) < 3:
        return len(s)

    # Hashmap to store the rightmost position of each character in the current window
    char_map = {}
    left, max_len = 0, 0

    # Sliding window approach with the right pointer
    for right in range(len(s)):
        # Add the current character to the hashmap
        char_map[s[right]] = right

        # If there are more than two distinct characters
        if len(char_map) > 2:
            # Find the leftmost character in the window to remove
            leftmost = min(char_map.values())
            del char_map[s[leftmost]]  # Remove it from the dictionary
            left = leftmost + 1  # Move the left pointer to shrink the window

        # Calculate the length of the current window
        max_len = max(max_len, right - left + 1)

    return max_len

s = "eceba"
print(lengthOfLongestSubstringTwoDistinct(s))  # Output: 3 ("ece")


def lengthOfLongestSubstringTwoDistinct(s):
    if len(s) < 3:
        return len(s)

    # Create a list of size 128 to store the count of characters in the current window
    char_count = [0] * 128
    left = 0
    max_len = 0
    distinct_count = 0

    for right in range(len(s)):
        # Add the current character to the window
        if char_count[ord(s[right])] == 0:
            distinct_count += 1
        char_count[ord(s[right])] += 1

        # If we have more than two distinct characters, shrink the window
        while distinct_count > 2:
            char_count[ord(s[left])] -= 1
            if char_count[ord(s[left])] == 0:
                distinct_count -= 1
            left += 1

        # Update the maximum length of the valid substring
        max_len = max(max_len, right - left + 1)

    return max_len
