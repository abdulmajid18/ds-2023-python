class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Count the frequency of each character using map.get()
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Step 2: Find the first unique character by checking frequencies
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index

        # Step 3: If no unique character is found, return -1
        return -1
