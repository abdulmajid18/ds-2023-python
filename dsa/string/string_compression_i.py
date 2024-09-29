from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0  # This pointer will write the compressed version
        left = 0  # This pointer marks the start of the current group

        for right in range(n):
            # Check if we are at the end of the group (end of array or next character is different)
            if right == n - 1 or chars[right] != chars[right + 1]:
                # Write the character to the `write` pointer
                chars[write] = chars[left]
                write += 1

                # If the group is more than 1 character long, write the count
                if right - left + 1 > 1:
                    count = str(right - left + 1)
                    for c in count:
                        chars[write] = c
                        write += 1

                # Move the left pointer to the next new character
                left = right + 1

        # Return the length of the compressed array
        return write
