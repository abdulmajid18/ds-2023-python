class Solution:
    def length_of_longest_substring(self, string):
        count = [0] * 256
        i, num_distinct, max_length = 0, 0, 0

        for j in range(len(string)):
            char = ord(string[j])
            if count[char] == 0:
                num_distinct += 1
            count[char] += 1
            while num_distinct > 2:
                count[char] -= 1
                if count[char] == 0:
                    num_distinct -= 1
                i += 1
            max_length = max(max_length, j - i + 1)
        return max_length
