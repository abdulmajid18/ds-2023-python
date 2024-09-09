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
