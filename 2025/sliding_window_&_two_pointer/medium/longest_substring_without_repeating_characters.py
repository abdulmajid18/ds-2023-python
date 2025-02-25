class Solution:

    def lengthOfLongestSubstringBruteForce(self, s: str) -> int:
        """
        Brute Force Approach:
        ---------------------
        - Generate all substrings using two nested loops.
        - Check if each substring has unique characters using a set.
        - Update the maximum length found.

        Complexity Analysis:
        --------------------
        - Outer loop runs `O(n)`, inner loop runs `O(n)`, and checking uniqueness takes `O(n)`.
        - Overall time complexity: **O(n³)**.
        - Space complexity: **O(n)** (for storing unique characters in a set).

        Example:
        --------
        Input: "abcabcbb"
        - Possible substrings: ["a", "ab", "abc", "b", "bc", "bca", "c", "ca", ...]
        - Maximum length = 3 ("abc")

        Edge Cases:
        -----------
        - Empty string → Return 0.
        - Single character → Return 1.
        - All unique characters → Return `len(s)`.
        """

        n = len(s)
        max_length = 0  # Stores the length of the longest valid substring

        for i in range(n):  # Start of substring
            for j in range(i, n):  # End of substring
                substring = s[i:j + 1]  # Extract substring
                if len(set(substring)) == len(substring):  # Check uniqueness
                    max_length = max(max_length, len(substring))

        return max_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Thought Process:
        ----------------
        - We need to find the longest substring without repeating characters.
        - A sliding window approach (two-pointer technique) is optimal.
        - We maintain a `set` to store unique characters in the current window.
        - The left pointer `l` starts at the beginning and moves forward only when we detect a duplicate.
        - The right pointer `r` expands the window by iterating through the string.
        - If a duplicate is found:
            - Remove characters from the left (`l`) until the duplicate is gone.
            - Move `l` forward.
        - Update the maximum length of the substring at each step.

        Complexity Analysis:
        -------------------
        - Each character is added and removed from the set at most once → O(n) time complexity.
        - The `set` operations (add/remove) take O(1) time on average.
        - Space complexity is O(min(n, 26)) = O(1), as there are at most 26 unique characters (for lowercase English letters).

        Example Walkthrough:
        --------------------
        Input: "abcabcbb"

        Step-by-step:
        1. 'a' → Set: {'a'}, res = 1
        2. 'b' → Set: {'a', 'b'}, res = 2
        3. 'c' → Set: {'a', 'b', 'c'}, res = 3
        4. 'a' (duplicate) → Remove 'a', move l → Set: {'b', 'c', 'a'}, res = 3
        5. 'b' (duplicate) → Remove 'b', move l → Set: {'c', 'a', 'b'}, res = 3
        ...
        Final result = 3

        Edge Cases:
        ----------
        - Empty string (`""`) → Return 0.
        - String with all unique characters (`"abcdef"`) → Return length of the string.
        - String with repeated characters (`"bbbbb"`) → Return 1.
        """

        l = 0
        res = 0
        hash_set = set()

        for r, v in enumerate(s):
            while v in hash_set:
                hash_set.remove(s[l])
                l += 1

            res = max(res, r - l + 1)
            hash_set.add(v)

        return res
